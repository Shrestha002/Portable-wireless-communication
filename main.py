import serial
import time
import comm1

def send_file_to_serial_port(file_path, serial_port, baudrate):
    try:
        data_packet_manager = comm1.DataPacketManager()
        data_packet_manager.generate_packets_from_file(file_path)
        data_packet_manager.write_packets_to_file("output_packets.dat")

        ser = serial.Serial(port=serial_port, baudrate=baudrate)
        with open("output_packets.dat", "rb") as file:
            while True:
                chunk = file.read(64)
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
        received_data = bytearray()

        while True:
            data = ser.read(64)
            if not data:
                break
            received_data.extend(data)

        ser.close()

        with open(file_path, "wb") as file:
            file.write(received_data)

        print(f"File received and saved to {file_path}.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    action = input("Enter 'send' to send a file or 'receive' to receive a file: ")
    file_path = input("Enter the path to the file: ")
    serial_port = input("Enter the serial port name (e.g., COM1, /dev/ttyUSB0): ")

    if action == "send":
        send_file_to_serial_port(file_path, serial_port, baudrate=9600)
    elif action == "receive":
        receive_file_from_serial_port(file_path, serial_port, baudrate=9600)
