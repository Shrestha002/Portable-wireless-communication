import threading
import serial
import time

from PySide6.QtWidgets import QApplication
class BroadcastChannel:
    def __init__(self, serial,isInBroadcast ):
        self.ser = serial
        self.isInBroadcast = isInBroadcast

    
    def start_monitoring(self):
        if self.isInBroadcast:
            print("Already monitoring.")
            return

        # Start monitoring thread
        
        self.isInBroadcast = True
        monitoring_thread = threading.Thread(target=self.monitor_broadcast)
        try:
            
            monitoring_thread.start()
        except Exception:
            print(Exception)
            monitoring_thread.stop()

    def stop_monitoring(self):
        self.isInBroadcast = False
    
    def monitor_broadcast(self):
        if not self.ser:
            raise Exception("Serial port not connected.")
        try:
            while self.isInBroadcast:
                # Check if DTR pin is False
                if True:   #not self.ser.dtr:
                    # Read exactly 64 bytes
                    data = self.ser.readline()
                    
                    print("Received Data (64 bytes):", data)
                    data =data.decode(errors='ignore')
                    
                    # Handle different types of packets based on the first byte
                    packet_type = data[0]
                    if packet_type<='9' and packet_type>='0':
                        payload = data[1:]
                        print(packet_type," ,, ",payload)
                        if packet_type == '0':
                            # Device identification packet
                            device_id = payload[:5]
                            device_name = payload[5:]
                            print("Device ID:", device_id)
                            print("Device Name:", device_name)
                            # Do something with device ID and name
                        
                        elif packet_type == '1':
                            # Connection request packet
                            print("Received Connection Request Packet")
                            # Handle connection request
                        
                        elif packet_type == 2:
                            # ACK packet
                            print("Received ACK Packet")
                            # Handle ACK
                    else:
                        print("AT response: ",data)
        except Exception as e:
            print("\nKeyboard interrupt detected. Stopping monitoring.", e)
            self.isInBroadcast = False    
            # Add more cases for different packet types as needed

            time.sleep(0.1)  # Sleep for a short interval to avoid busy-waiting

    def discoverability_on(self,address,name):
        if not self.ser:
            raise Exception("Serial port not connected.")
        self.ser.setDTR(False)
        data_packet = "0{:0<5}{:0<10}\r\n".format(address, name)
        for i in range(10):
            
            self.ser.write(data_packet.encode())
            time.sleep(0.5)
            response = self.ser.read_all().decode()
            print("Packet sent:", data_packet)
            time.sleep(0.5)
            QApplication.processEvents()

    def connect_device(self, device_id):
        if not self.ser:
            raise Exception("Serial port not connected.")
        
        command = "AT+B{} \r\n".format(device_id)
        self.ser.write(command.encode())
        time.sleep(0.5)
        response = self.ser.read_all().decode()
        return response

    def handle_connect_request(self):
        if not self.ser:
            raise Exception("Serial port not connected.")
        
        self.ser.write(b"AT+RX\r\n")
        time.sleep(0.5)
        response = self.ser.read_all().decode()
        return response

    def change_channel(self, channel):
        self.ser.setDTR(True)
        if not self.ser:
            raise Exception("Serial port not connected.")
        time.sleep(1)
        command = "AT+C{:03d}\r\n".format(channel)
        print(command)
        self.ser.flush()
        self.ser.write(command.encode())
        time.sleep(1)
        response = self.ser.read_all().decode()
        self.ser.setDTR(False)
        return response

    def change_baudrate(self, baudrate):
        self.ser.setDTR(True)
        if not self.ser:
            raise Exception("Serial port not connected.")
        time.sleep(1)
        command = "AT+B{}\r\n".format(baudrate)
        self.ser.flush()
        self.ser.write(command.encode())
        time.sleep(1)
        response = self.ser.read_all().decode()
        self.ser.setDTR(False)
        return response
'''
# Example Usage
# Assuming the HC-12 module is connected to COM3 with baudrate 9600
broadcast = BroadcastChannel(serial_port='COM6', baudrate=9600)
broadcast.connect_serial()

# Scan for devices
print("Scanning devices:")
print(broadcast.scan_devices())

# Turn discoverability on
print("Turning discoverability on:")
print(broadcast.discoverability_on())

# Connect to device with ID 123
print("Connecting to device 123:")
print(broadcast.connect_device(123))

# Change channel to 34


broadcast.start_monitoring()
time.sleep(5)
print("Changing channel to 34:")
i=1
#while i<90:
#    print(broadcast.change_channel(i))
#    i=i+1
#    time.sleep(5)
# Let the monitoring run for some time

# Stop monitoring

#broadcast.discoverability_on(12.34,'MyDevice')
#broadcast.scan_devices()
#broadcast.disconnect_serial()
'''