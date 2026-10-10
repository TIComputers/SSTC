from prompt_toolkit.application import Application
from prompt_toolkit.layout import (
    Window,
    HSplit,
    ScrollablePane,
    FormattedTextControl,
    Layout,
)
from prompt_toolkit.widgets import (
    TextArea,
    Frame,
    Label
)
from datetime import datetime
from key import Set_Key
import shutil
import os


class View:
    def __init__(self, chat, box, log, styl):
        self.chat = chat
        self.box  = box
        self.log  = log
        self.styl = styl
        

        self.display_box = Window(
            content=FormattedTextControl(
                text=self.__get_fbox,
                style="bold white",
            ),
            wrap_lines=True,
        )

        self.scroll = ScrollablePane(
            self.display_box,
            show_scrollbar=True,
            keep_cursor_visible=False,
        )

        self.input_area = TextArea(
            prompt=" << ",
            multiline=True,
            wrap_lines=True,
            height=1,
            style="bold white",
        )

        self.status_bar = Label(
            text=self.__get_status,
            style=f"bold {self.styl}",
        )
        
        self.container = HSplit([
            Frame(
                title=self.__get_time,
                body=self.scroll,
                style=f"bold {self.styl}",
            ),
            Frame(
                title="INPUT BOX",
                body=self.input_area,
                style="bold white",
            ),
            self.status_bar,
        ])


    def __terminal_size(self):
        try:
            terminal_size = shutil.get_terminal_size()
            lines = terminal_size.lines
            return lines -5
        except OSError:
            lines = int(os.environ.get('LINES', 24))
            return lines -5


    def __get_fbox(self):
        formatted = []
        sindex = max(
            
             0,
            self.chat.spos - self.__terminal_size()
        )
        eindex = min(
        len(self.chat.gbox),
            self.chat.spos,
        )
        for index in range(sindex, eindex):
            txt = self.chat.gbox[index]
            formatted.append(
                f"{txt[1]} {txt[0]} {txt[2]}"
            )
        return "\n".join(formatted)


    def __get_status(self):
        return(
            f"Message:{len(self.chat.gbox)} |"
            f"Scroll: {self.chat.spos}/{len(self.chat.gbox)}"
            "Keys: Ctrl+↑/↓=Scroll, Enter=Send, Ctrl+Q=Quit"
        )


    def __get_time(self):
        Time = datetime.now()
        return Time.strftime("%Y/%m/%d %H:%M:%S")



class Tui:
    def __init__(self, chat, box, flag, log, styl):
        self.chat = chat
        self.flag = flag
        self.styl = styl
        
        self.box  = box
        self.log  = log
        self.keys = None

        self.view = View(
            self.chat,
            self.box ,
            self.log ,
            self.styl,
        )

        self.keys = Set_Key(
            self.flag,
            self.log,
        )
        
        self.app = None


    def __config(self):
        self.app = Application(
            layout=Layout(
                self.view.container,
            ),
            key_bindings=self.keys.Keys(
                self.chat,
                self.view.input_area,
            ),
            full_screen=True,
            mouse_support=True,
            refresh_interval=0.1,
        )
        self.log.write("(tui) config called")


    def start(self):
        self.__config()
        self.log.write("(tui) app started")
        self.app.run()

if __name__ == "__main__":
    pass