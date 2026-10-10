from prompt_toolkit.key_binding import KeyBindings

class Set_Key:
    def __init__(self, flag, log):
        self.flag = flag
        self.log  = log


    def Keys(self, chat, inpa):
        kb = KeyBindings()

        @kb.add("c-q")
        def _(event):
            self.log.write("(key) c-q")
            self.flag.shutdown()
            event.app.exit()

        @kb.add("enter")
        def _(event):
            text = inpa.text.strip()
            if text:
                chat.upload(text)
                inpa.text = ""
                self.log.write(f"(key) enter:{text}")
                event.app.invalidate()


        @kb.add("c-up")
        def _(event):
            chat.scroll_up()
            event.app.invalidate()

        @kb.add("c-down")
        def _(event):
            chat.scroll_down()
            event.app.invalidate()

        @kb.add("home")
        def _(event):
            chat.spos = 0
            event.app.invalidate()

        @kb.add("end")
        def _(event):
            chat.scroll_to_bottom()
            event.app.invalidate()

        return kb

if __name__ == "__main__":
    pass