from datetime import datetime
import os

class Log:
    def __init__(self):
        self.file = ""
        self.path = "./log/"
        self.__check_path()
        self.__file_name()


    def __time(slef):
        time = datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{time}] "


    def __file_name(self):
        time = datetime.now()
        time = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.file = time + ".txt"


    def __check_path(self):
        if not os.path.exists("log"):
            os.mkdir("log")


    def write(self, log):
        log = self.__time() + log
        with open(self.path + self.file, "a") as file:
            file.write(log + "\n")
            
if __name__ == "__main__":
    pass