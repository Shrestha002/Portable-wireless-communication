## run this.. This is final
import os
import sys
import threading
import time
import tempfile
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar, QPushButton,QApplication, QMainWindow, QLabel, QVBoxLayout, QSizePolicy, QMessageBox, QFileDialog
from PySide6.QtCore import Qt, Signal, QThread,Slot, QTimer, QTime
import pyaudio
import wave
import pygame
import serial.tools.list_ports
from FilePayloadManager import FilePayloadManager
from PacketManager import PacketManager
from backend import Backend
from exp import Ui_MainWindow
import resources_rc
import simpleaudio as sa
from pydub import AudioSegment
class SerialThread(QThread):
    messageReceived = Signal(str)
    fileProgress = Signal(int)
    fileTransferCompleted = Signal(str)
    mp3Received = Signal(str)
    def __init__(self,address):
        super().__init__()
        self.mainWindow = MainWindow
        self.port = None
        self.baudrate = None
        self.backend = None
        self.running = True
        self.listener_thread = None
        self.Packet_Manager = PacketManager()
        self.filePayloadmanager = FilePayloadManager()
        self.address = address
    def run(self):
        pass

    def connectSer(self,port,baudrate):
        self.backend = Backend(serialport=port, baudrate=baudrate, address=self.address, name="Sunirban")
        status = self.backend.connectSerial()
        if status == "connected":
            self.start_listening_thread()
        else:
            raise status

    def start_listening_thread(self):
        self.listener_thread = threading.Thread(target=self.listen_serial)
        self.listener_thread.start()

    def listen_serial(self):
        file_payload = []
        isHeader = True
        total_packet = 0
        while self.running:
            print("listing")
            if self.backend:
                try:
                    try:
                        packet = self.backend.get_Packet()
                    except Exception as e:
                        print("Error while receiving packet: "+str(e))
                    print(len(packet))
                    if packet:
                        try:
                            packet_type, device_address, receiver_address, payload = self.Packet_Manager.decode_packet(packet)
                            print(packet_type)
                        except Exception as e:
                            print("error at packet decoding: "+ str(e))
                        if packet_type == self.Packet_Manager.PACKET_TYPE_TEXT:
                            if receiver_address == self.address or receiver_address == "Broad":
                                self.messageReceived.emit(payload)
                        elif packet_type == self.Packet_Manager.PACKET_TYPE_FILE:
                            #print(payload)
                            #add here logic to open a popup to show progress
                            if isHeader:
                                total_packet,filename = self.filePayloadmanager.parse_header_packet(payload)
                                file_payload.append(payload)
                                total_packet = int(total_packet.decode())
                                self.fileProgress.emit(0)
                                #self.progress_dialog = ProgressBarDialog(total_packet, self.mainWindow)
                                #self.progress_dialog.show()
                                isHeader = False
                            else:
                                try:
                                    packet_no, data_byte = self.filePayloadmanager.parse_data_packet(payload)
                                #self.progress_dialog.update_progress(len(self.file_payload) - 1)
                                    packet_no = int(packet_no.decode())
                                    self.fileProgress.emit((packet_no*100/total_packet))
                                    file_payload.append(payload)
                                except Exception as e:
                                    print("Error at parsing data pkt: "+str(e))
                                print("Packet No: "+ str(packet_no))
                                if packet_no == total_packet:
                                    try:
                                        filePath = self.filePayloadmanager.write_payloads_to_file('\\ReceivedFiles',file_payload)
                                        self.fileTransferCompleted.emit('\\ReceivedFiles')
                                    except Exception as e:
                                        print("Error while writing"+str(e))
                                    isHeader = True
                                    file_payload.clear()
                                    if filename.lower().endswith('.mp3'):
                                        self.mp3Received.emit(filePath)

                except Exception as e:
                    print(str(e)+" in listen")
                    
              # Add a small delay to prevent high CPU usage

    
    def send_message(self, message,address):
        if self.backend:
            self.backend.send_text_to_serial(message,address)
    
    def send_file(self,filename):
        try:
            self.fileProgress.emit(1000)
            self.backend.send_file_to_serial(filename,"Broad")
            
            return 1
        except Exception as e:
            print(e)
            return 0
        
    def stop(self):
        self.running = False
        if self.backend:
            self.backend.ser.close()
        self.wait()



class SendOptionsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Send Options")
        self.setModal(True)
        
        self.layout = QVBoxLayout()

        self.broadcast_button = QPushButton("Broadcast")
        self.broadcast_button.clicked.connect(self.broadcast_message)
        self.layout.addWidget(self.broadcast_button)

        self.device1_button = QPushButton("Device1")
        self.device1_button.clicked.connect(self.send_to_device1)
        self.layout.addWidget(self.device1_button)

        self.device2_button = QPushButton("Device2")
        self.device2_button.clicked.connect(self.send_to_device2)
        self.layout.addWidget(self.device2_button)

        self.setLayout(self.layout)
        self.mainWindow = parent

    def broadcast_message(self):
        self.mainWindow.send_message("Broad")
        self.accept()

    def send_to_device1(self):
        self.mainWindow.send_message("33.33")
        self.accept()

    def send_to_device2(self):
        self.mainWindow.send_message("11.11")
        self.accept()
class RecordingThread(QThread):
    recordingStopped = Signal(list)

    def __init__(self, audio, sample_rate=16000):
        super().__init__()
        self.audio = audio
        self.sample_rate = sample_rate
        self.frames = []
        self.running = True

    def run(self):
        stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=self.sample_rate, input=True, frames_per_buffer=1024)
        while self.running:
            data = stream.read(1024)
            self.frames.append(data)
        stream.stop_stream()
        stream.close()
        self.recordingStopped.emit(self.frames)

    def stop(self):
        self.running = False

class MP3Popup(QDialog):
    def __init__(self, parent=None, mp3_file_path=""):
        super().__init__(parent)
        self.setWindowTitle("MP3 File Received")

        self.mp3_file_path = mp3_file_path

        layout = QVBoxLayout()

        message_label = QLabel("MP3 file received. Do you want to play it?")
        layout.addWidget(message_label)

        play_button = QPushButton("Play")
        play_button.clicked.connect(self.play_mp3)
        layout.addWidget(play_button)

        self.setLayout(layout)

    def play_mp3(self):
        pygame.init()

        # Load the MP3 file
        pygame.mixer.music.load(self.mp3_file_path)

        # Play the MP3 file
        pygame.mixer.music.play()

        # Wait for the MP3 to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

class MicrophoneDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Microphone Recorder")
        self.setModal(True)
        
        self.recording_thread = None
        self.audio = pyaudio.PyAudio()
        self.sample_rate = 16000
        self.frames = []
        self.play_obj = None
        
        self.layout = QVBoxLayout()

        self.timer_label = QLabel("00:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.timer_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time = QTime(0, 0)

        self.record_button = QPushButton("Record")
        self.record_button.clicked.connect(self.start_recording)
        self.layout.addWidget(self.record_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_recording)
        self.layout.addWidget(self.stop_button)

        self.play_button = QPushButton("Play")
        self.play_button.setEnabled(False)
        self.play_button.clicked.connect(self.play_recording)
        self.layout.addWidget(self.play_button)

        self.send_button = QPushButton("Send")
        self.send_button.setEnabled(False)
        self.send_button.clicked.connect(self.send_recording)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def start_recording(self):
        self.recording_thread = RecordingThread(self.audio, self.sample_rate)
        self.recording_thread.recordingStopped.connect(self.on_recording_stopped)
        self.recording_thread.start()
        
        self.timer.start(1000)
        self.record_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.send_button.setEnabled(False)
        
    def stop_recording(self):
        if self.recording_thread:
            self.recording_thread.stop()
            self.recording_thread.wait()

        self.timer.stop()
        self.record_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.play_button.setEnabled(True)
        self.send_button.setEnabled(True)

    def on_recording_stopped(self, frames):
        self.frames = frames

    def play_recording(self):
        if self.play_obj is not None:
            self.play_obj.stop()

        wave_obj = sa.WaveObject.from_wave_file("recording.wav")
        self.play_obj = wave_obj.play()

    def send_recording(self):
        self.save_recording("recording.wav")
        self.convert_to_mp3("recording.wav", "recording.mp3")
        self.accept()  # Close the dialog

    def update_timer(self):
        self.time = self.time.addSecs(1)
        self.timer_label.setText(self.time.toString("mm:ss"))

    def save_recording(self, filename):
        # Compress the recorded audio frames using μ-law encoding
        #compressed_frames = audioop.lin2ulaw(b''.join(self.frames), 2)
        
        # Save the compressed audio data to a WAV file
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))  # μ-law compressed data has 1-byte width
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(self.frames))
    def convert_to_mp3(self, wav_filename, mp3_filename):
        # Load the WAV file
        audio = AudioSegment.from_wav(wav_filename)
        AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
        # Export as MP3 (or you can choose another format like OGG)
        audio.export(mp3_filename, format="mp3", bitrate="10k")  # 32 kbps bitrate for smaller file size

    def closeEvent(self, event):
        if self.recording_thread and self.recording_thread.isRunning():
            self.recording_thread.stop()
            self.recording_thread.wait()
        self.audio.terminate()
        event.accept()
class MainWindow(QMainWindow):
    def __init__(self):
        self.backend = None
        #Backend(serialport="COM15", baudrate=115200,address="12.34",name="Sunirban")

        super(MainWindow, self).__init__()
        
        #self.backend.listen_to_serial()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Send.clicked.connect(self.open_send_options_dialog)
        self.ui.Search.clicked.connect(self.start_scanning)
        self.ui.Discoveribility.clicked.connect(self.toggDiscov)
        self.ui.Refresh.clicked.connect(self.refresh_ports)
        self.ui.ConnectComPort.clicked.connect(self.connect_to_port)
        self.ui.Files.clicked.connect(self.openFiles)
        self.baudRate = int(self.ui.BaudInpt.currentText())
        self.ui.Microphone.clicked.connect(self.open_microphone_dialog)
        #self.ui.widget_3.mouseDoubleClickEvent.connect(self.setToDev1)
        #self.ui.TogglePower.clicked.connect(self.toggelPower)
        self.serial_thread = None
        self.serial_thread = SerialThread("22.22")
        self.serial_thread.mp3Received.connect(self.open_mp3_popup)
        self.serial_thread.start()
        self.serial_thread.messageReceived.connect(self.add_received_label)
        self.serial_thread.fileProgress.connect(self.update_progress_bar)
        self.serial_thread.fileTransferCompleted.connect(self.on_file_transfer_completed)
    def open_mp3_popup(self, filepath):
        # Open the popup window with the main window as its parent
        popup_window = MP3Popup(self,filepath)
        popup_window.show()
    def open_microphone_dialog(self):
        microphone_dialog = MicrophoneDialog(self)
        microphone_dialog.exec()
        # Handle the recorded file if needed
        if microphone_dialog.result() == QDialog.Accepted:
            filename = "recording.mp3"
            if os.path.exists(filename):
                if self.serial_thread.backend:
                    self.serial_thread.send_file(filename)
                    QMessageBox.information(self, "File Sent", f"{filename} has been sent successfully.")
                else:
                    QMessageBox.warning(self, "Connection Warning", "Please select a COM port")
            else:
                QMessageBox.warning(self, "File Error", "Recorded file not found.")

    def open_send_options_dialog(self):
        send_options_dialog = SendOptionsDialog(self)
        send_options_dialog.exec()

    
    def openFiles(self):
        file_dialog = QFileDialog()
        filename, _ = file_dialog.getOpenFileName(self, "Open File", "", )
        file_size = os.path.getsize(filename)

        print(os.path.basename(filename),file_size)
        if file_size > 1024*1024:
            QMessageBox.warning(self, "File size Warning", "Please select a smaller file")
            return
        else:
            if self.serial_thread.send_file(filename):
                QMessageBox.information(self, "Connection Status", f"File sent successfully")
            else:
                QMessageBox.warning(self, "Error", "An error occured while sending")

       

    def refresh_ports(self):
        self.ui.ComList.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.ComList.addItem(port.device)

    def connect_to_port(self):
        selected_port = self.ui.ComList.currentText()
        bd = int(self.ui.BaudInpt.currentText())
        supported_baudrate = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
        if bd not in supported_baudrate:
            
            QMessageBox.warning(self, "Connection Warning", f"{bd} Baudrate is not supported! \nchoose between these 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200")
            return
        self.baudRate = bd
        if selected_port:
            try:
                
                self.serial_thread.connectSer(selected_port, self.baudRate)
                QMessageBox.information(self, "Connection Status", f"Connected to {selected_port}")
            except Exception as e:
                QMessageBox.critical(self, "Connection Error", f"{e}\n ")
        else:
            QMessageBox.warning(self, "Connection Warning", "Please select a COM port")



    def send_message(self,target):
        message_text = self.ui.MessageBox.toPlainText()
        if self.serial_thread.backend :
            
            self.serial_thread.send_message(message_text,target)
            self.add_sent_label(message_text)
            self.ui.MessageBox.clear()
            self.ui.MessageBox.setFocus()
            #self.serial_thread.messageReceived.emit("Test message")
        else:
            QMessageBox.warning(self, "Connection Warning", "Please select a COM port")


    def toggDiscov(self):
        self.workerThread = threading.Thread(target=self.toggle_discoverability)
        # Schedule the termination of the thread after 5 seconds
        self.workerThread.start()

        # Wait for the thread to finish
        self.workerThread.join()

    def toggle_discoverability(self):
        
            self.backend.toggleDiscoverability()
            # Add a small delay to avoid excessive CPU usage
            time.sleep(0.1)
    def add_sent_label(self, message_text):
        self.add_label(message_text, "Send")
    
    
    @Slot(str)
    def add_received_label(self, message_text):   
        print("inside Slot")     
        self.add_label(message_text, "Receive")

    


    def add_label(self, message_text,role):
        if role!= "Send":
            print("align Right")
            alignment = Qt.AlignRight
        else:
            print("align Left")
            alignment = Qt.AlignLeft
        #message_text = self.ui.MessageBox.toPlainText()
        if len(message_text) == 0:
            return
        # Create a new QLabel with the message text
        label = QLabel(message_text)
        label.setStyleSheet("""
        background-image: url(assets/bg.bmp);
        border-radius: 10px; /* Rounded corners */
        border: 1px solid #ccc; /* Border */
        padding: 8px; /* Padding inside the label */
        """)
        label.setMaximumWidth(700)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        
          # Set the maximum width
        # Enable word wrap to allow the label to increase height to fit multiple lines
        label.setWordWrap(True)

        layout = self.ui.scrollAreaWidgetContents.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
            layout.addStretch()  # Add a spacer item to push contents to the top
            self.ui.scrollAreaWidgetContents.setLayout(layout)

        # Add the label to the layout of the scroll area's contents widget
        layout.insertWidget(layout.count() - 1, label)  # Insert before the spacer
        layout.setAlignment(label, alignment | Qt.AlignTop)
         # Automatically scroll to the bottom
        self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())
    
    def update_progress_bar(self, value):
        if value == 1000:
            self.ui.ShowProgress.setText("Sending file...")
        elif value:
            self.ui.ShowProgress.setText(f"{value}% ..Received")

    def on_file_transfer_completed(self, directory):
        
            self.ui.ShowProgress.setText("")
            QMessageBox.information(self, "File Transfer", f"File received and saved to {directory}")

    def start_scanning(self):
        return
    
    def closeEvent(self, event):
        if self.serial_thread:
            self.serial_thread.stop()
            self.serial_thread.wait()  # Ensure the thread has completely stopped
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
