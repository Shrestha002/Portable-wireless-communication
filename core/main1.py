import serial
import time
import comm1
import os
data_packet_manager = comm1.DataPacketManager()

def send_file_to_serial_port(file_path, serial_port, baudrate):
    try:
        file_name = os.path.basename(file_path)
        file_extension = os.path.splitext(file_name)[1]
        print(f"::File name: {file_name}, Extension: {file_extension}::")
        data_packet_manager.generate_packets_from_file(file_path)
        data_packet_manager.write_packets_to_file("output_packets.dat")

        ser = serial.Serial(port=serial_port, baudrate=baudrate)
        ser.setDTR(False)
        time.sleep(1)
        FILENAME=f"::{file_name}::\n"
        # Send filename and extension
        ser.write(FILENAME.encode())
        
        time.sleep(1)
        with open("output_packets.dat", "rb") as file:
            while True:
                chunk = file.read(data_packet_manager.size())
                if not chunk:
                    break
                ser.write(chunk)
                time.sleep(0.1)  # Add a small delay to ensure data transmission

        ser.close()

        print("File sent to serial port successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

def receive_file_from_serial_port( serial_port, baudrate):
    try:
        ser = serial.Serial(port=serial_port, baudrate=baudrate)
        ser.setDTR(False)
        
        # Read filename and extension
        initial_data = ser.readline()
        print(initial_data)
        # file_info_start = initial_data.find("::") + len("::")
        # file_info_end = initial_data.find("::")

        # file_name = initial_data[file_info_start:file_info_end]
        # file_extension = initial_data[file_info_end + len(", Extension: "):-2]
        
        file_path = "rec_"+initial_data[2:-3].decode() 
        print(file_path)
        file = open(str(file_path), "wb")

        while True:
            packet = ser.read(data_packet_manager.size())
            
            if not packet:
                break

            packet_number, total_length, total_packets, data_bytes = data_packet_manager.parse_data_packet(packet)
            print(f"{packet_number} of {total_packets} received. {round(((packet_number * 100.00) / total_packets),2)}% complete")

            file.write(data_bytes)
            if packet_number == total_packets:
                print(f"File received and saved to {file_path}.")
                file.close()
                ser.close()
                break
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    action = input("Enter 'send' to send a file or 'receive' to receive a file: ")
    file_path = input("Enter the path to the file: ")
    serial_port = input("Enter the serial port name (e.g., COM1, /dev/ttyUSB0): ")

    if action == "send":
        send_file_to_serial_port(file_path, serial_port, baudrate=115200)
    elif action == "receive":
        receive_file_from_serial_port( serial_port, baudrate=115200)
