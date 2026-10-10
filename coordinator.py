from dispather import Dispather
from protocol import Protocol
from threading import Thread
from box import MailBox
from time import sleep
from chat import Chat
from pipe import Pipe
from log import Log
from tui import Tui

class Coordinator:
    def __init__(self, host, port, mode, them, tout):
        self.log  = Log()
        self.box  = MailBox()

        self.HOST = host
        self.PORT = port
        self.mode = mode
        self.them = them
        
        self.zone = None
        self.tout = tout

        self.sock = None
        self.pipe = None
        self.addr = None
        self.chat = None
        self.flag = None


    def run(self):
        self.__socket()
        self.__create_flag()
        self.__protocol()
        self.__create_chat()
        self.__dispather()
        self.__tui()


    def __socket(self):
        sock = Pipe(
            self.HOST,
            self.PORT,
            self.mode,
            self.log ,
            self.tout,
        )
        self.sock = sock.sock


    def __create_flag(self):
        self.flag = State(
            self.sock
        )


    def __protocol(self):
        self.pipe = Protocol(
            self.sock,
            self.flag,
            self.log ,
        )


    def __create_chat(self):
        self.chat = Chat(
            self.box,
            self.log,
        )


    def __dispather(self):
        secretary = Dispather(
            self.pipe,
            self.chat,
            self.box ,
            self.flag,
            self.log ,
        )
        self.__thread(secretary)


    def __thread(self, obj):
        t1 = Thread(
            target = obj.life_cycle
        )
        t1.start()
        self.log.write("(Coordinator) Thread started")


    def __tui(self):
        terminal_ui = Tui(
            self.chat,
            self.box ,
            self.flag,
            self.log ,
            self.them,
        )
        sleep(0.5)
        terminal_ui.start()


class State:
    def __init__(self, sock):
        self.sock  = sock
        self.state = True


    def check_state(self):
        return self.state


    def shutdown(self):
        self.state = False
        sleep(0.3)
        self.sock.close()


if __name__ == "__main__":
    host = input("IP: ")
    port = int(input("PORT: "))
    mode = int(input("MODE (listner:1 / client:0): "))
    obj = Coordinator(
        host,
        port,
        mode,
    )
    
    obj.run()
    