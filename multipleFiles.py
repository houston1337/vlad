from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import numpy as np
from tkinter.messagebox import showerror


class multipleFile(Toplevel):
    def __init__(self, master, callback, file_path=""):
        super().__init__(master)
        self.callback = callback
        self.title("Выбрать файл")
        self.button = ttk.Button(self, text="Выбрать файлы", command=self.select_files, padding=5)
        self.button.grid(row=0, column=0, padx=10, )
        self.buttonAdd = ttk.Button(self, text="Добавить", command=self.addFiles, padding=5)
        self.buttonAdd.grid(row=0, column=1, padx=10, )

    xS = []
    yS = []

    def select_files(self):
        self.selectedFiles = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=(("Text Files", "*.csv"), ("All Files", "*.*")),
        )

        index = 2
        xLabel = ttk.Label(self, text="Столбец X")
        xLabel.grid(row=1, column=1)
        yLabel = ttk.Label(self, text="Столбец Y")
        yLabel.grid(row=1, column=2, padx=10)
        for filename in self.selectedFiles:
            fileLabel = ttk.Label(self, text=os.path.basename(filename))
            fileLabel.grid(row=index, column=0)

            xColumn = StringVar(value=0)
            xColumnNumber = Spinbox(self, from_=0, to=10, width=5, textvariable=xColumn)
            xColumnNumber.grid(row=index, column=1, sticky=W)
            self.xS.append(xColumnNumber)

            yColumn = StringVar(value=1)
            yColumnNumber = Spinbox(self, from_=0, to=10, width=5, textvariable=yColumn)
            yColumnNumber.grid(row=index, column=2, sticky=W)
            self.yS.append(yColumnNumber)
            index += 1

    def addFiles(self):
        for index in range(len(self.selectedFiles)):
            self.read_file(self.selectedFiles[index], index)

    def read_file(self, file, index):
        try:
            allDataFromFile = np.genfromtxt(file, delimiter=";", dtype=(float))
            X = allDataFromFile[:, int(self.xS[index].get())]
            Y = allDataFromFile[:, int(self.yS[index].get())]
            self.master.createNewGraph(x=X, y=Y)
        except:
            showerror('Ошибка', "Ошибка чтения файла -" + os.path.basename(
                file) + " Проверьте путь до файла или наличие столбца в файле")

    # def printNumber(self):
