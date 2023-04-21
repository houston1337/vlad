from tkinter import *
from tkinter import filedialog


class Files(Toplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.title("Выбрать файлы")
        button = Button(self, text="Select Files", command=self.select_files)
        button.pack()

    def select_files(self):
        self.selectedFiles = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=(("Text Files", "*.csv"), ("All Files", "*.*"))
        )
        self.send_data()

    def send_data(self):
        fileStr = self.selectedFiles[0]
        self.callback([fileStr])
        # self.master.readFile()



