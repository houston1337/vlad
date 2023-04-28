from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import numpy as np
from tkinter.messagebox import showerror


class SingleFile(Toplevel):
    def __init__(self, master, callback, file_path=""):
        super().__init__(master)
        self.callback = callback
        self.title("Выбрать файл")
        self.geometry("200x100")
        self.button = ttk.Button(self, text="Выбрать файл", command=self.select_files, padding=5)
        self.button.grid(row=0, column=0, columnspan=2)
        self.selectedFiles = [file_path]
        xColumn = StringVar(value=0)
        self.xColumnLabel = ttk.Label(self, text="Столбец для оси Х", justify=LEFT)
        self.xColumnLabel.grid(row=1, column=0, sticky=W, pady=5)
        self.xColumnNumber = Spinbox(self, from_=0, to=10, width=5, textvariable=xColumn, command=self.send_data)
        self.xColumnNumber.grid(row=1, column=1, sticky=W)

        yColumn = StringVar(value=1)
        self.yColumnLabel = ttk.Label(self, text="Столбец для оси Х", justify=LEFT)
        self.yColumnLabel.grid(row=2, column=0, sticky=W)
        self.yColumnNumber = Spinbox(self, from_=0, to=10, width=5, textvariable=yColumn, command=self.send_data)
        self.yColumnNumber.grid(row=2, column=1, sticky=W)

    X = []
    Y = []

    def select_files(self):
        self.selectedFiles = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=(("Text Files", "*.csv"), ("All Files", "*.*")),
        )
        print(type(self.selectedFiles))
        self.send_data()

    def send_data(self):
        self.read_file()
        self.fileStr = self.selectedFiles
        self.callback([self.X, self.Y])
        # self.master.readFile()

    def read_file(self):
        try:
            self.allDataFromFile = np.genfromtxt(self.selectedFiles[0], delimiter=";", dtype=(float))
            self.X = self.allDataFromFile[:, int(self.xColumnNumber.get())]
            self.Y = self.allDataFromFile[:, int(self.yColumnNumber.get())]
        except:
            showerror('Ошибка', "Ошибка чтения файла. Проверьте путь до файла или наличие столбца в файле")
        # print(self.isUseFile.get())
