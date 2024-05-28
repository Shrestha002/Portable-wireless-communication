import os
import sys
import threading
import time
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar, QPushButton,QApplication, QMainWindow, QLabel, QVBoxLayout, QSizePolicy, QMessageBox, QFileDialog
from PySide6.QtCore import Qt, Signal, QThread,Slot

import serial.tools.list_ports
from FilePayloadManager import FilePayloadManager
from PacketManager import PacketManager
from backend import Backend
from exp import Ui_MainWindow
import resources_rc

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
                                # add logic here if filename is mp3 type
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
            self.backend.send_file_to_serial(filename,"33.33")
            
            return 1
        except Exception as e:
            print(e)
            return 0
        
    def stop(self):
        self.running = False
        if self.backend:
            self.backend.ser.close()
        self.wait()
chatHistory = []


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
        self.mainWindow.send_message("22.22")
        self.accept()


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
        self.ui.Microphone.clicked.connect(self.handleMic)
        #self.ui.widget_3.mouseDoubleClickEvent.connect(self.setToDev1)
        #self.ui.TogglePower.clicked.connect(self.toggelPower)
        self.serial_thread = None
        self.serial_thread = SerialThread("11.11")
        self.serial_thread.start()
        self.serial_thread.messageReceived.connect(self.add_received_label)
        self.serial_thread.fileProgress.connect(self.update_progress_bar)
        self.serial_thread.fileTransferCompleted.connect(self.on_file_transfer_completed)
    def handleMic(self):
        pass
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
