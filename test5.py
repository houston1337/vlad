from tkinter import *
from tkinter import ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import customtkinter as ctk
from line import Lines
from OX import OXname
from singleFile import SingleFile
from graphSettings import GraphSettings
from multipleFiles import multipleFile


class App(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("995x773")
        self.title("VApp")
        ctk.set_appearance_mode("dark")

        self.fTop = LabelFrame(text="Добавление данных")
        self.fTop.grid_columnconfigure(0, weight=1)
        self.fTop.grid_columnconfigure(1, weight=1)
        self.fTop.grid_columnconfigure(2, weight=1)
        self.fTop.grid_columnconfigure(4, weight=1)
        self.function_label = ttk.Label(self.fTop, text="Введите функцию:", justify=LEFT)
        self.function_label.grid(row=0, column=0, sticky=W, padx=12)

        self.strFunc = StringVar()
        self.strFunc.set("x")
        self.functionField = ttk.Entry(self.fTop, width=20, textvariable=self.strFunc, justify=LEFT)
        self.functionField.bind("<Return>", self.gen_graph2)
        self.functionField.grid(row=0, column=1, sticky=W)

        self.addNew = ttk.Button(self.fTop, text="Добавить новый", width=20, command=self.createNewGraph)
        self.addNew.grid(row=0, column=2, sticky=W)

        self.goToLabel = ttk.Label(self.fTop, text="Перейти к:", justify=LEFT)
        self.goToLabel.grid(row=0, column=3, sticky=W)
        self.goTo = StringVar()
        self.goTo.set(0)
        self.goToField = ttk.Entry(self.fTop, width=5, textvariable=self.goTo, justify=LEFT)
        self.goToField.grid(row=0, column=4)
        self.goToButton = ttk.Button(self.fTop, text="ok", command=self.set_curret)
        self.goToButton.grid(row=0, column=5, sticky=W)

        self.buildButton = ttk.Button(self.fTop, text="Построить", command=self.gen_graph)
        self.buildButton.grid(row=1, column=5, ipadx=77, ipady=6)

        self.intervalStartLabel = ttk.Label(self.fTop, text="Начало интервала a:", justify=LEFT)
        self.intervalStartLabel.grid(row=1, column=0, sticky=W, padx=12)
        self.strA = StringVar()
        self.strA.set(0)
        self.start = ttk.Entry(self.fTop, width=10, textvariable=self.strA)
        self.start.grid(row=1, column=1, sticky=W)

        self.intervalEndLabel = Label(self.fTop, width=15, height=2, text="Конец интервала b:", justify=LEFT)
        self.intervalEndLabel.grid(row=1, column=2, sticky=W)
        self.strB = StringVar()
        self.strB.set(10)
        self.end = ttk.Entry(self.fTop, width=10, textvariable=self.strB)
        self.end.grid(row=1, column=3, sticky=W)

        self.importLabel = Label(self.fTop, text="Файл с \nтабличными значениями", justify=LEFT)
        self.importLabel.grid(row=2, column=0, sticky=W, padx=12)
        self.importBtn = ttk.Button(self.fTop, text="Добавить файл", width=20, command=self.read_from_file)
        self.importBtn.grid(row=2, column=1, sticky=W)

        self.strFile = StringVar()
        self.strFile.set("C:/Users/Egor/Desktop/vlad/data/ampl1.csv")
        self.fileField = ttk.Entry(self.fTop, width=20, textvariable=self.strFile)
        self.fileField.bind("<Return>", self.gen_graph2)
        self.fileField.grid(row=2, column=2, sticky=W)

        self.isUseFile = BooleanVar()
        self.useDataFromFile = ttk.Checkbutton(self.fTop, text="Использовать данные из файла", variable=self.isUseFile)
        self.useDataFromFile.grid(row=2, column=5, sticky=W)

        self.batchLabel = Label(self.fTop, text="Пакетная обработка", justify=LEFT)
        self.batchLabel.grid(row=3, column=0, sticky=W, padx=12, pady=10)
        self.batchBtn = ttk.Button(self.fTop, text="Добавить файлы", width=20, command=self.open_multi)
        self.batchBtn.grid(row=3, column=1, sticky=W)

        self.strFiles = StringVar()
        self.strFiles.set("ampl1.csv, ampl2.csv ...")
        self.filesField = ttk.Entry(self.fTop, width=20, textvariable=self.strFiles)
        self.filesField.grid(row=3, column=2, sticky=W)

        self.isDrawAll = BooleanVar()
        self.DrawAll = ttk.Checkbutton(self.fTop, text="Построить все", variable=self.isDrawAll)
        self.DrawAll.grid(row=3, column=5, sticky=W)

        self.fTop.pack(side=TOP, fill=X, padx=10, pady=10)

        # добавление раздела для настройки элементов графика (цвет, формат)

        self.fBottom = LabelFrame(text="Настройка элементов графика")

        self.linesLabel = Label(self.fBottom, text="Линии", borderwidth=5)
        self.linesLabel.grid(row=0, column=0, padx=5, pady=5)
        self.linesBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_lines)
        self.linesBtn.grid(row=0, column=1, padx=5, pady=5)

        self.backgroundLabel = Label(self.fBottom, text="Фон", borderwidth=5)
        self.backgroundLabel.grid(row=1, column=0, padx=5, pady=5)
        self.backgroundBtn = ttk.Button(self.fBottom, text="Настроить")
        self.backgroundBtn.grid(row=1, column=1, padx=5, pady=5)

        self.xAxisLabel = Label(self.fBottom, text="Ось X", borderwidth=5)
        self.xAxisLabel.grid(row=2, column=0, padx=5, pady=5)
        self.xAxisBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_OX)
        self.xAxisBtn.grid(row=2, column=1, padx=5, pady=5)

        self.yAxisLabel = Label(self.fBottom, text="Ось Y", borderwidth=5)
        self.yAxisLabel.grid(row=3, column=0, padx=5, pady=5)
        self.yAxisBtn = ttk.Button(self.fBottom, text="Настроить")
        self.yAxisBtn.grid(row=3, column=1, padx=5, pady=5)

        self.headerLabel = Label(self.fBottom, text="Заголовок", borderwidth=5)
        self.headerLabel.grid(row=4, column=0, padx=5, pady=5)
        self.headerBtn = ttk.Button(self.fBottom, text="Настроить")
        self.headerBtn.grid(row=4, column=1, padx=5, pady=5)

        self.gridLabel = Label(self.fBottom, text="Сетка", borderwidth=5)
        self.gridLabel.grid(row=5, column=0, padx=5, pady=5)
        self.gridBtn = ttk.Button(self.fBottom, text="Настроить")
        self.gridBtn.grid(row=5, column=1, padx=5, pady=5)

        self.legendLabel = Label(self.fBottom, text="Легенда ", borderwidth=5)
        self.legendLabel.grid(row=7, column=0, padx=5, pady=5)
        self.legendBtn = ttk.Button(self.fBottom, text="Настроить")
        self.legendBtn.grid(row=7, column=1, padx=5, pady=5)

        self.fBottom.pack(side=RIGHT, fill=Y, padx=10, pady=10)

        self.fDown = LabelFrame()

        self.clearBtn = ttk.Button(self.fDown, text="Очистить", command=self.clear)
        self.clearBtn.grid(row=0, column=0, padx=5, pady=5)

        self.saveBtn = ttk.Button(self.fDown, text="Сохранить изображение", command=self.save)
        self.saveBtn.grid(row=0, column=1, padx=5, pady=5)

        # self.l9 = Button(self.fDown, text="Сохранить в файл", borderwidth=5)
        # self.l9.grid(row=0, column=2, padx=5, pady=5)
        self.fDown.pack(side=BOTTOM, padx=[10, 10], pady=[10, 10])

        self.fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
        self.ax = self.fig.add_subplot(111)
        self.canvasAgg = FigureCanvasTkAgg(self.fig, master=self)
        self.canvasAgg.draw()
        self.canvas = self.canvasAgg.get_tk_widget()
        self.canvas.pack(fill=BOTH, expand=1)

    currentGraphIndex = 0
    lastAddedIndex = 0
    graphs = np.array([GraphSettings(X=[], Y=[])])

    def open_lines(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].color, \
            self.graphs[self.currentGraphIndex].line_type, \
            self.graphs[self.currentGraphIndex].line_thick = data

        Lines(self, callback)

    def open_OX(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].x_label_text, \
            self.graphs[self.currentGraphIndex].x_label_fontsize, \
            self.graphs[self.currentGraphIndex].x_label_color = data
            print(data)

        OXname(self, callback)

    def open_multi(self):
        def callback(data):
            print(data)

        multipleFile(self, callback)

    def read_from_file(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].X, \
            self.graphs[self.currentGraphIndex].Y = data
        SingleFile(self, callback, self.strFile.get())

    def save(self):
        self.after(100, self.gen_graph)
        self.canvasAgg.print_figure('1.jpg')

    def clear(self):
        self.ax.clear()
        self.canvasAgg.draw()

    # def defineX(self):
    #     if (not (self.isUseFile.get())):
    #         self.graphs[self.currentGraphIndex].X = np.linspace(a, b, 5)

    def gen_graph(self):
        try:
            a = float(self.start.get())
            b = float(self.end.get())
            # print(str(a) + " " + str(b))
            # если используется строка ввода функции
            if (not (self.isUseFile.get())):
                self.graphs[self.currentGraphIndex].func = self.functionField.get()
                exec('f = lambda x:' + self.graphs[self.currentGraphIndex].func, globals())
                self.graphs[self.currentGraphIndex].X = np.linspace(a, b, 5)
                self.graphs[self.currentGraphIndex].Y = [f(x) for x in self.graphs[self.currentGraphIndex].X]
            # если используем файл
            # else:
            # X = linspace(a, b, self.Y.shape[0])

            self.ax.clear()  # очистить графическую область

            if (self.isDrawAll.get()):
                for graph in self.graphs:
                    self.ax.plot(
                        graph.X,
                        graph.Y,
                        color=graph.color,
                        linestyle=graph.line_type,
                        linewidth=graph.line_thick)
            else:
                self.ax.plot(
                    self.graphs[self.currentGraphIndex].X,
                    self.graphs[self.currentGraphIndex].Y,
                    color=self.graphs[self.currentGraphIndex].color,
                    linestyle=self.graphs[self.currentGraphIndex].line_type,
                    linewidth=self.graphs[self.currentGraphIndex].line_thick)

            self.ax.set_xlabel(
                self.graphs[self.currentGraphIndex].x_label_text,
                fontsize=self.graphs[self.currentGraphIndex].x_label_fontsize,
                color=self.graphs[self.currentGraphIndex].x_label_color)
            self.canvasAgg.draw()  # перерисовать «составной» холст
            return
        except:  # реакция на любую ошибку
            showerror('Ошибка', "Неверное выражение или интервал [a,b].")

    def gen_graph2(self, event):  # чтобы кнопка отжималась при ошибке
        self.after(100, self.gen_graph)

    def print_current(self):
        print(self.graphs[self.currentGraphIndex].X)
        print(self.graphs[self.currentGraphIndex].color)
        print(self.graphs[self.currentGraphIndex].Y)

    def createNewGraph(self, x=[], y=[]):
        self.strFunc.set("")
        self.strFile.set("")
        self.lastAddedIndex += 1
        self.currentGraphIndex = self.lastAddedIndex
        self.graphs = np.append(self.graphs, [GraphSettings(X=x, Y=y)])
        self.print_current()

    def set_curret(self):
        self.print_current()
        if (self.goTo.get() < str(0) or self.goTo.get() > str(self.lastAddedIndex)):
            showerror('Ошибка', "Графика не найдено")
        else:
            self.currentGraphIndex = int(self.goTo.get())
            self.strFunc.set(self.graphs[self.currentGraphIndex].func)
            self.strFile.set(self.graphs[self.currentGraphIndex].file)

    def printAll(self):
        for graph in self.graphs:
            print("func ", graph.func)
            print("X ", graph.X)
            print("Y ", graph.Y)

            print("color ", graph.color)
            print("line_type ", graph.line_type)
            print("line_thick ", graph.line_thick)
            print("\n_______________________________________________\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
