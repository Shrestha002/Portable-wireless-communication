import serial
import time
import comm1
data_packet_manager = comm1.DataPacketManager()
def send_file_to_serial_port(file_path, serial_port, baudrate):
    try:
        
        data_packet_manager.generate_packets_from_file(file_path)
        data_packet_manager.write_packets_to_file("output_packets.dat")

        ser = serial.Serial(port=serial_port, baudrate=baudrate)
        ser.setDTR(False)
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

def receive_file_from_serial_port(file_path, serial_port, baudrate):
    try:
        ser = serial.Serial(port=serial_port, baudrate=baudrate)
        ser.setDTR(False)
        received_data = bytearray()
        file=open(file_path, "wb")
        while True:
            packet = ser.read(data_packet_manager.size())
            
            if not packet:
                break
            received_data.extend(packet)
            packet_number, total_length, total_packets, data_bytes = data_packet_manager.parse_data_packet(packet)
            print(f" {packet_number} of {total_packets} received. {(packet_number*100.00)/total_packets}% complete")

            file.write(data_bytes)
            if(packet_number==total_packets):
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
        receive_file_from_serial_port(file_path, serial_port, baudrate=115200)
