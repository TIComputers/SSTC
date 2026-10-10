from colorama import Fore
import socket


class Pipe:
    def __init__(self, host, port, mode, log, tout):
        self.sock = None
        self.addr = None       
        self.HOST = host
        self.PORT = port
        self.MODE = mode
        self.log  = log
        self.tout = tout
        
        self.__excute() 


    def __create(self):
        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )


    def __listener(self):
        try:
            self.sock.bind((
                self.HOST,
                self.PORT,
            ))
            self.sock.listen()
            self.sock.settimeout(
                self.tout
            )
            
            text1 = f"\n[?] {self.tout} sec Listening to {self.HOST}:{self.PORT}"
            self.log.write(text1)
            print(Fore.RED + text1 + Fore.RESET)

            
            client, addr = self.sock.accept()
            self.sock.close()
            self.sock = client

            text2 = f"[#] Connected {addr[0]}:{addr[1]}"
            print(Fore.RED + text2 + Fore.RESET)
        
        except TimeoutError:
            text2 = "[!] Listening Finished"
            self.log.write(text2)
            # print()    
            exit(Fore.RED + text2 + Fore.RESET)


    def __connect(self):
        try:
            self.sock.connect((
                self.HOST,
                self.PORT
            ))
            self.log.write(f"Connected to {self.HOST}:{self.PORT}")
            print(Fore.RED + f"Connected to {self.HOST}" + Fore.RESET)
        
        except ConnectionRefusedError:
            text3 = "[!] User Not Exsist"
            self.log.write(text3)    
            exit(Fore.RED + text3 + Fore.RESET)
            
    def __check_mode(self):
        if self.MODE == "listen":
            self.__listener()
        elif self.MODE == "client":
            self.__connect()
        else:
            print(Fore.RED + "[!] Please Try Again" + Fore.RESET)        


    def __blocking(self):
        self.sock.setblocking(False)


    def __excute(self):
        self.__create()
        self.__check_mode()
        self.__blocking()
        self.log.write(
            f"(Pipe) socket NonBlocking"
        )

    
if __name__ == "__main__":
    pass