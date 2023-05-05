from tkinter import *
from tkinter import ttk

class Info(Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.text = Text(self, width=100, height=50)
        self.text.insert(1.0, "Hello world!\nline two")
        self.text.tag_add('title', 1.0, '1.end')
        self.text.tag_config('title', justify=CENTER,
                        font=("Verdana", 24, 'bold'))
        self.text.pack()