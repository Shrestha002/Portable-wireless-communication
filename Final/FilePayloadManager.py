import os
import struct

class FilePayloadManager:
    data_format = "4s 128s"    # Data structure: <4_byte_packet_number>:<128_byte_data_chunk>
    header_format = "4s 128s"  # Header structure: <4_byte_total_packet_number>:<name_with_extension>

    def __init__(self):
        self.payloads = []
        self.total_payloads = 0

    def create_data_packet(self, packet_number, data):
        # Ensure data is bytes
        if isinstance(data, str):
            data_bytes = data.encode()
        else:
            data_bytes = data

        # Pad the data to 128 bytes if necessary
        if len(data_bytes) < 128:
            data_bytes = data_bytes.ljust(128, b'\x00')

        packet_number_str = f"{packet_number:04}"

        # Convert the packet number to bytes
        packet_number_bytes = packet_number_str.encode()
        # Pack the packet
        packet = struct.pack(self.data_format, packet_number_bytes, data_bytes)
        return packet

    def parse_data_packet(self, packet):
        packet_number, data_bytes = struct.unpack(self.data_format, packet)
        return packet_number, data_bytes

    def create_header_packet(self, total_packets, filename):
        filename_bytes = filename.encode()

        # Pad the filename to 128 bytes if necessary
        if len(filename_bytes) < 128:
            filename_bytes = filename_bytes.ljust(128, b'\x00')

        total_packet_str = f"{total_packets:04}"

        # Convert the packet number to bytes
        total_packet_bytes = total_packet_str.encode()
        # Pack the header packet
        header_packet = struct.pack(self.header_format, total_packet_bytes, filename_bytes)
        return header_packet

    def parse_header_packet(self, packet):
        total_packets, filename_bytes = struct.unpack(self.header_format, packet)
        filename = filename_bytes.decode().strip('\x00')
        return total_packets, filename
     
    def trim_filename(self,filename, max_length=127):
        # Split the filename into base name and extension
        base_name, extension = filename.rsplit('.', 1)
        
        # Ensure the minimum length requirement
        if max_length <= len(extension) + 1:
            raise ValueError("Maximum length must be greater than the length of the extension plus 1.")
        
        # Calculate the maximum length allowed for the base name
        max_base_length = max_length - len(extension) - 1
        
        # Trim the base name if necessary
        if len(base_name) > max_base_length:
            base_name = base_name[:max_base_length]
        
        # Combine the trimmed base name with the extension
        new_filename = f"{base_name}.{extension}"
        
        return new_filename

    def generate_payloads_from_file(self, file_path):
        self.payloads = []
        file_size = os.path.getsize(file_path)
        self.total_payloads = (file_size + 127) // 128  # Calculate total packets (round up)

        # Create the header packet
        filename = os.path.basename(file_path)
        header_packet = self.create_header_packet(self.total_payloads,self.trim_filename(filename))
        self.payloads.append(header_packet)

        with open(file_path, 'rb') as file:
            packet_number = 1
            while True:
                data = file.read(128)
                if not data:
                    break

                packet = self.create_data_packet(packet_number, data)

                self.payloads.append(packet)
                packet_number += 1

        return self.payloads

    def write_payloads_to_file(self, output_file_path, received_packets):
        header_packet = received_packets[0]
        total_packets, filename = self.parse_header_packet(header_packet)
        #print(filename)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dest_dir = os.path.join(script_dir, 'ReceivedFiles')
        try:
            os.makedirs(dest_dir)
        except OSError:
            pass # already exists
        path = os.path.join(dest_dir, filename)
        #output_file_path = os.path.join(output_file_path, filename)
        print(path)
        with open(path, 'wb') as output_file:
            print("inside fopen")
            flag = False
            for packet in received_packets:

                _, data = self.parse_data_packet(packet)
                if flag:
                    #print(data.rstrip(b'\x00'))
                    output_file.write(data.rstrip(b'\x00'))  # Remove padding bytes
                flag = True
        return path

    def size(self):
        return struct.calcsize(self.data_format)
