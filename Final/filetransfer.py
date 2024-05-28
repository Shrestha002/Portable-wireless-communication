import serial
import time
from FilePayloadManager import FilePayloadManager

import os

from PacketManager import PacketManager


class FileTransferManager:
    def __init__(self, serial ,receiver,sender,file_path=None):
        self.ser = serial
        self.sender = sender
        self.receiver = receiver
        self.file_path = file_path
        self.file_payload = FilePayloadManager()
        self.packet_manager = PacketManager()
    def send_text(self,text):
        try:
            packet = self.packet_manager.form_packet(self.packet_manager.PACKET_TYPE_TEXT,self.sender,self.receiver,text)
            self.ser.setDTR(False)
            self.ser.write(packet)
            time.sleep(0.1)
        except Exception:
            print(Exception)

    def send_file_to_serial_port(self, file_path):
        try:
            payloads = self.file_payload.generate_payloads_from_file(file_path)
            self.ser.setDTR(False)
            time.sleep(1)
            for i in (payloads):
                packet = self.packet_manager.form_packet(self.packet_manager.PACKET_TYPE_FILE,"12.34","12.33",i)
                
                print(packet)
                self.ser.write(packet)
                time.sleep(0.1)
                #print(str((i*100)//len(payloads) ) + "% done")
            print("File sent to serial port successfully.")
        except Exception as e:
            print(f"Error: {str(e)}")
    '''
    def receive_file_from_serial_port(self):
        try:
          
            self.ser.setDTR(False)
            
            # Read filename and extension
            initial_data = self.ser.readline()
            print(initial_data)
            # file_info_start = initial_data.find("::") + len("::")
            # file_info_end = initial_data.find("::")

            # file_name = initial_data[file_info_start:file_info_end]
            # file_extension = initial_data[file_info_end + len(", Extension: "):-2]
            
            file_path = "rec_"+initial_data[2:-3].decode() 
            print(file_path)
            file = open(str(file_path), "wb")

            while True:
                packet = self.ser.read(data_packet_manager.size())
                
                if not packet:
                    break

                packet_number, total_length, total_packets, data_bytes = data_packet_manager.parse_data_packet(packet)
                print(f"{packet_number} of {total_packets} received. {round(((packet_number * 100.00) / total_packets),2)}% complete")

                file.write(data_bytes)
                if packet_number == total_packets:
                    print(f"File received and saved to {file_path}.")
                    file.close()
                
                    break
        except Exception as e:
            print(f"Error: {str(e)}")
    '''
# Assuming DataPacketManager is defined elsewhere

if __name__ == "__main__":

    
    action = input("Enter 'send' to send a file or 'receive' to receive a file: ")
    file_path = input("Enter the path to the file: ")
    serial_port = input("Enter the serial port name (e.g., COM1, /dev/ttyUSB0): ")
    
    serialport= serial.Serial(serial_port, 115200)
    filetransfer = FileTransferManager(serialport, file_path=file_path)
    if action == "send":
        filetransfer.send_file_to_serial_port(file_path)
    elif action == "receive":
        filetransfer.receive_file_from_serial_port( serial_port, baudrate=115200)
