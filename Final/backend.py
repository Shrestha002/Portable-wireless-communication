import serial
from PacketManager import PacketManager
from broadcast import BroadcastChannel
from filetransfer import FileTransferManager
class Backend:
    def __init__(self, serialport, baudrate,address, name):
        self.ser=None
        self.address = address
        self.name = name
        self.serialport=serialport
        self.baudrate=baudrate
        self.serConnected=False
        self.isInBroadcast = False
        self.discov = False
    
    #self.broadcastChannel= BroadcastChannel(self.ser)
      

    def connectSerial(self):
        try:
          self.ser=serial.Serial(self.serialport,self.baudrate)
          self.serConnected = True
          print("serial connected")
          self.ser.setDTR(False)
          return "connected"
        except Exception as e:
            print(e)
            return e
    def disconnectSerial(self):
        try:
            self.ser.close()
            self.serConnected = False
        except Exception:
            print(Exception)

    def listen_to_serial(self):
      Broadcast = BroadcastChannel(self.ser,isInBroadcast=True)
      Broadcast.start_monitoring()

    def toggleDiscoverability(self):
        print("Inside Toggle disc")
        if self.serConnected :
            print("Inside Toggle disc 1")
            Broadcast = BroadcastChannel(self.ser,isInBroadcast=False)
            Broadcast.discoverability_on(self.address, self.name)

    def send_text_to_serial(self,text,receiver):
        if self.serConnected:
            sender = FileTransferManager(self.ser,receiver,self.address)
            sender.send_text(text)
    def send_file_to_serial(self,file_path,receiver):
        if self.serConnected:
            sender = FileTransferManager(self.ser,receiver,self.address)
            sender.send_file_to_serial_port(file_path)
    def get_Packet(self):
        buffer = bytearray()
        print("new msg")
        sop_received = False
        
        while True:
            try:
                byte = self.ser.read(1)
                if not byte:
                    raise RuntimeError("Serial port read timeout")
                
                buffer.append(byte[0])
                
                if len(buffer) >= 4:
                    # Check if the last four bytes are SOP
                    if not sop_received and buffer[-4:] == PacketManager.SOP:
                        print("SOP received")
                        buffer = bytearray(PacketManager.SOP)  # Clear buffer but keep SOP
                        sop_received = True

                    # Check if the last four bytes are EOP
                    elif sop_received and buffer[-4:] == PacketManager.EOP:
                        print("EOP received")
                        return buffer
            except Exception as e:
                print(str(e)+" in get Packet")
                return

    def get_Packet1(self):
        
        buffer = bytearray()
        print("new msg")
        while True:
            try:
                #self.ser.flush()
                byte = self.ser.read(1)
                #print(byte)
                if not byte:
                    raise RuntimeError("Serial port read timeout")
                if byte == b'\x01':
                    print("Byffer ckeared")
                    buffer.clear()
                buffer.append(byte[0])
                #print(buffer)
                if byte == b'\x04':
                    print("sop received")
                    return buffer
                    break
            except Exception as e:
                    print(e)
                    return

        return buffer
            
