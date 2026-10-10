
class MailBox:
    def __init__(self):
        self.send_queue = []
        self.recv_queue = []


    def input_send_queue(self, text):
        self.send_queue.insert(0, text)


    # dispather
    def output_send_queue(self): 
        text = self.send_queue[-1]
        self.send_queue.pop()
        return text


    # dispather
    def check_send_queue(self):
        if self.send_queue:
            return True
        else:
            return False

    # ---------------------------------------------

    # dispather
    def input_recv_queue(self, text): 
        self.recv_queue.insert(0, text)


    def output_recv_queue(self):
        text = self.recv_queue[-1]
        self.recv_queue.pop()
        return text


    def check_recv_queue(self):
        if self.recv_queue:
            return True
        else:
            return False

if __name__ == "__main__":
    pass