from math import ceil
import os
import struct

class DataPacketManager:
    packet_format = "I H H 32s"

    def __init__(self):
        self.packets = []
        self.total_packets = 0

    def create_data_packet(self, packet_number, total_length, total_packets, data):
        if isinstance(data, str):
            data_bytes = data.encode()
        else:
            data_bytes = data
        packet = struct.pack(self.packet_format, packet_number, total_length, total_packets, data_bytes)
        return packet

    def parse_data_packet(self, packet):
        packet_number, total_length, total_packets, data_bytes = struct.unpack(self.packet_format, packet)
        #data = data_bytes.decode()
        return packet_number, total_length, total_packets, data_bytes

    def generate_packets_from_file(self, file_path):
        self.packets = []
        file_size = os.path.getsize(file_path)
        
        with open(file_path, 'rb') as file:
            packet_number = 1

            while True:
                data = file.read(32)
                if not data:
                    break

                total_length = len(data) + struct.calcsize(self.packet_format)
                self.total_packets =ceil(file_size/32)

                packet = self.create_data_packet(packet_number, total_length, self.total_packets, data)
                self.packets.append(packet)
                packet_number += 1
                

    def write_packets_to_file(self, output_file_path):
        with open(output_file_path, 'wb') as output_file:
            for packet in self.packets:
                output_file.write(packet)
    def size(self):
        return struct.calcsize(self.packet_format)
        
    def read_packets_from_file(self, file_path):
        with open(file_path, 'rb') as file:
            read_packets = []
            while True:
                packet = file.read(struct.calcsize(self.packet_format))
                print(packet)
                if not packet:
                    break
                read_packets.append(packet)
            return read_packets

if __name__ == "__main__":
    data_packet_manager = DataPacketManager()
    input_file_path = "file.txt"
    output_file_path = "output_packets.dat"

    data_packet_manager.generate_packets_from_file(input_file_path)
    data_packet_manager.write_packets_to_file(output_file_path)


    read_packets = data_packet_manager.read_packets_from_file(output_file_path)
    for i, packet in enumerate(read_packets):
        packet_number, total_length, total_packets, data = data_packet_manager.parse_data_packet(packet)
        print(f"Read Packet {packet_number}: Total Length={total_length}, Total Packets={total_packets}, Data={data}")
