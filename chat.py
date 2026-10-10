from datetime import datetime

class Chat:
    def __init__(self, box, log):
        self.gbox = []
        self.spos = 0
        
        self.box = box
        self.log = log


    def __get_time(self):
        Time = datetime.now()
        return Time.strftime("%H:%M:%S")


    def upload(self, text):
        self.gbox.append([
            "<<",
            self.__get_time(),
            text,
        ])
        self.scroll_to_bottom()
        self.box.input_send_queue(text)
        self.log.write(f"(Tui.Chat) Uploaded:{text}")


    def download(self, text):
        self.gbox.append([
            ">>",
            self.__get_time(),
            text,
        ])
        self.scroll_to_bottom()
        self.log.write(f"(Tui.Chat) Downloaded:{text}")


    def scroll_to_bottom(self):
        self.spos = len(self.gbox)


    def scroll_up(self):
        if self.spos > 0:
            self.spos = max(
                0,
                self.spos -1
            )


    def scroll_down(self):
        if self.spos < len(self.gbox):
            self.spos = min(
                len(self.gbox),
                self.spos +1
            )


if __name__ == "__main__":
    pass