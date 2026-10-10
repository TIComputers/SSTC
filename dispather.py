from time import sleep

class Dispather:
    def __init__(self, pipe, chat, box, flag, log):
        self.pipe = pipe
        self.chat = chat
        self.box  = box
        self.flag = flag
        self.log  = log


    def life_cycle(self):

        try:
            while self.flag.check_state():

                text = self.pipe.recive()

                if text != None:
                    if text != "":
                        self.box.input_recv_queue(text)
                        self.chat.download(text)
                        self.log.write(f"(Dispather) save to recivebox:{text}")
                        sleep(0.003)
                    else:
                        self.chat.download("User disconnected")
                        self.flag.shutdown()

                if self.box.check_send_queue():
                    data = self.box.output_send_queue()
                    self.pipe.send(data)
                    self.log.write(f"(Dispather) data sended: {data}")
                    sleep(0.003)

                sleep(0.003)

            self.log.write("(Dispather) finish life_cycle")


        except Exception as e:
            self.flag.shutdown()
            self.log.write(f"(Dispather) Error:{e}")

if __name__ == "__main__":
    pass