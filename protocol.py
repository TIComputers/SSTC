import struct
import random

class Protocol:
    def __init__(self, sock, flag, log):
        self.sock = sock
        self.flag = flag
        self.log  = log
        
        self.HEADER_STRUCT = struct.Struct("!B")
        self.MAX_PACKET_SIZE = self.HEADER_STRUCT.size
    
    
    def recive(self):
        try:
            data = self.sock.recv(512)
            
            if data == b"":
                self.log.write("(Protocol) Connectoin closed")
                
            data = data.decode()
            
            if data != None:
                self.log.write(f"(Protocol) recived:{data}")
                return data
                
            else:
                return None

        except BlockingIOError:
            return None
        
        except Exception as e:
            self.log.write(f"(Protocol) Error:{e}")


    def send(self, text):
        text = text.encode()
        self.sock.sendall(text)
        self.log.write(f"(Protocol) sended:{text}")        
        
        
        
if __name__ == "__main__":
    pass
        
        
        
    # for update
    # def __get_number_message(self):
    #     return random.randint(60, 90)
    
    # insert a protocol for recive and send 
    # insert encryption and decryption
