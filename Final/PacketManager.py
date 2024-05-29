# from numpy import char


# class PacketManager:
#     SOH = 0x01  # Start of Heading
#     STX = 0x02  # Start of Text
#     ETX = 0x03  # End of Text
#     EOP = 0x04  # End of Packet

#     PACKET_TYPE_CONFIGURATION = '0'
#     PACKET_TYPE_TEXT = '1'
#     PACKET_TYPE_FILE = '2'
#     PACKET_TYPE_ACK = '3'

#     ACK_POSITIVE = 0x06  # Positive Acknowledgment
#     ACK_NEGATIVE = 0x15  # Negative Acknowledgment

#     def __init__(self):
#         pass

#     def form_packet(self, packet_type, device_address, receiver_address, payload):
#         if len(device_address) != 5 or len(receiver_address) != 5:
#             raise ValueError("Device and receiver addresses must be 5 characters long")

#         packet = bytearray()
#         packet.append(self.SOH)
#         packet.extend(packet_type.encode('utf-8'))
#         packet.extend(device_address.encode('utf-8'))
#         packet.extend(receiver_address.encode('utf-8'))

#         if packet_type == self.PACKET_TYPE_CONFIGURATION:
#             packet.extend(payload.encode('utf-8'))
#         elif packet_type == self.PACKET_TYPE_TEXT:
#             packet.append(self.STX)
#             packet.extend(payload.encode('utf-8'))
#             packet.append(self.ETX)
#         elif packet_type == self.PACKET_TYPE_FILE:
#             packet.extend(payload)  # Payload should be a bytes-like object
#         elif packet_type == self.PACKET_TYPE_ACK:
#             packet.append(payload)

#         packet.append(self.EOP)
#         return packet

#     def decode_packet(self, packet):
#         if packet[0] != self.SOH or packet[-1] != self.EOP:
#             raise ValueError("Invalid packet format")

#         packet_type = chr(packet[1])
        
#         device_address = packet[2:7].decode('utf-8')
#         receiver_address = packet[7:12].decode('utf-8')
#         payload = None

#         if packet_type == self.PACKET_TYPE_CONFIGURATION:
#             payload = packet[12:-1].decode('utf-8')
#         elif packet_type == self.PACKET_TYPE_TEXT:
#             if packet[12] != self.STX or packet[-2] != self.ETX:
#                 raise ValueError("Invalid text packet format")
#             payload = packet[13:-2].decode('utf-8')
#         elif packet_type == self.PACKET_TYPE_FILE:
#             payload = packet[12:-1]  # Payload is raw bytes
#         elif packet_type == self.PACKET_TYPE_ACK:
#             payload = packet[12]

#         return packet_type, device_address, receiver_address, payload

# # Example usage
# if __name__ == "__main__":
#     pm = PacketManager()

#     # Form a text packet
#     text_packet = pm.form_packet(
#         PacketManager.PACKET_TYPE_TEXT,
#         device_address="mod12",
#         receiver_address="mod34",
#         payload="Hello, World!"
#     )
#     print(f"Formed Text Packet: {text_packet}")

#     # Decode the text packet
#     packet_type, device_address, receiver_address, payload = pm.decode_packet(text_packet)
#     print(f"Decoded Packet Type: {packet_type}")
#     print(f"Device Address: {device_address}")
#     print(f"Receiver Address: {receiver_address}")
#     print(f"Payload: {payload}")
class PacketManager:
    SOP = b'\x02\x02\x02\x02'  # Start of Packet
    EOP = b'\x04\x04\x04\x04'  # End of Packet

    PACKET_TYPE_CONFIGURATION = '0'
    PACKET_TYPE_TEXT = '1'
    PACKET_TYPE_FILE = '2'
    PACKET_TYPE_ACK = '3'

    ACK_POSITIVE = 0x06  # Positive Acknowledgment
    ACK_NEGATIVE = 0x15  # Negative Acknowledgment

    def __init__(self):
        pass

    def form_packet(self, packet_type, device_address, receiver_address, payload):
        if len(device_address) != 5 or len(receiver_address) != 5:
            raise ValueError("Device and receiver addresses must be 5 characters long")

        packet = bytearray()
        packet.extend(self.SOP)
        packet.extend(packet_type.encode('utf-8'))
        packet.extend(device_address.encode('utf-8'))
        packet.extend(receiver_address.encode('utf-8'))

        if packet_type == self.PACKET_TYPE_CONFIGURATION:
            packet.extend(payload.encode('utf-8'))
        elif packet_type == self.PACKET_TYPE_TEXT:
            packet.append(0x02)
            packet.extend(payload.encode('utf-8'))
            packet.append(0x03)
        elif packet_type == self.PACKET_TYPE_FILE:
            packet.extend(payload)  # Payload should be a bytes-like object
        elif packet_type == self.PACKET_TYPE_ACK:
            packet.append(payload)

        packet.extend(self.EOP)
        return packet

    def decode_packet(self, packet):
        if packet[:4] != self.SOP or packet[-4:] != self.EOP:
            raise ValueError("Invalid packet format")

        packet_type = chr(packet[4])
        
        device_address = packet[5:10].decode('utf-8')
        receiver_address = packet[10:15].decode('utf-8')
        payload = None

        if packet_type == self.PACKET_TYPE_CONFIGURATION:
            payload = packet[15:-4].decode('utf-8')
        elif packet_type == self.PACKET_TYPE_TEXT:
            if packet[15] != 0x02 or packet[-5] != 0x03:
                raise ValueError("Invalid text packet format")
            payload = packet[16:-5].decode('utf-8')
        elif packet_type == self.PACKET_TYPE_FILE:
            payload = packet[15:-4]  # Payload is raw bytes
        elif packet_type == self.PACKET_TYPE_ACK:
            payload = packet[15]

        return packet_type, device_address, receiver_address, payload
