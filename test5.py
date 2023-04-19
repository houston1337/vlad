from tkinter import *
from tkinter import ttk
from numpy import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import customtkinter as ctk
from line import Lines
from OX import OXname
from numpy import genfromtxt


class App(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("995x773")
        self.title("VApp")
        ctk.set_appearance_mode("dark")

        self.f_top = LabelFrame(text="Добавление данных")

        self.function_label = Label(self.f_top, width=15, height=2, text="Введите функцию:", anchor='w')
        self.function_label.grid(row=0, column=0, columnspan=1)

        self.strFunc = StringVar()
        self.strFunc.set("x")
        self.functionField = Entry(self.f_top, width=47, textvariable=self.strFunc)
        self.functionField.bind("<Return>", self.Gen_graph2)
        self.functionField.grid(row=0, column=2, columnspan=3)

        self.buildButton = Button(self.f_top, text="Построить", borderwidth=5, command=self.Gen_graph)
        self.buildButton.grid(row=0, column=5, ipadx=77, ipady=6, rowspan=3)


        self.intervalStartLabel = Label(self.f_top, width=15, height=2, text="Начало \nинтервала a:", anchor='w')
        self.intervalStartLabel.grid(row=1, column=0)
        self.strA = StringVar()
        self.strA.set(0)
        self.strA = Entry(self.f_top, width=5, textvariable=self.strA)
        self.strA.grid(row=1, column=1)

        self.intervalEndLabel = Label(self.f_top, width=15, height=2, text="Конец \nинтервала b:")
        self.intervalEndLabel.grid(row=1, column=2)
        self.strB = StringVar()
        self.strB.set(10)
        self.strB = Entry(self.f_top, width=3, textvariable=self.strB)
        self.strB.grid(row=1, column=3)

        self.importLabel = Label(self.f_top, width=25, height=2, text="Импортировать данные\n из файла")
        self.importLabel.grid(row=2, column=0, columnspan=1)
        self.importBtn = Button(self.f_top, text="Добавить файл", borderwidth=5, command=self.read_from_file)
        self.importBtn.grid(row=2, column=2)


        self.useFile = BooleanVar()
        self.useDataFromFile = Checkbutton(self.f_top, text="Использовать данные из файла", variable=self.useFile)
        self.useDataFromFile.grid(row=2, column=4)

        self.f_top.pack(side=TOP, fill=BOTH, padx=[10, 10], pady=[10, 10])

        # добавление раздела для настройки элементов графика (цвет, формат)

        self.f_bot = LabelFrame(text="Настройка элементов графика")

        self.linesLabel = Label(self.f_bot, text="Линии", borderwidth=5)
        self.linesLabel.grid(row=0, column=0, padx=5, pady=5)
        self.linesBtn = Button(self.f_bot, text="Настроить", borderwidth=2, command=self.open_lines)
        self.linesBtn.grid(row=0, column=1, padx=5, pady=5)

        self.backgroundLabel = Label(self.f_bot, text="Фон", borderwidth=5)
        self.backgroundLabel.grid(row=1, column=0, padx=5, pady=5)
        self.backgroundBtn = Button(self.f_bot, text="Настроить", borderwidth=2)
        self.backgroundBtn.grid(row=1, column=1, padx=5, pady=5)

        self.xAxisLabel = Label(self.f_bot, text="Ось X", borderwidth=5)
        self.xAxisLabel.grid(row=2, column=0, padx=5, pady=5)
        self.xAxisBtn = Button(self.f_bot, text="Настроить", borderwidth=2, command=self.open_OX)
        self.xAxisBtn.grid(row=2, column=1, padx=5, pady=5)

        self.yAxisLabel = Label(self.f_bot, text="Ось Y", borderwidth=5)
        self.yAxisLabel.grid(row=3, column=0, padx=5, pady=5)
        self.yAxisBtn = Button(self.f_bot, text="Настроить", borderwidth=2)
        self.yAxisBtn.grid(row=3, column=1, padx=5, pady=5)

        self.headerLabel = Label(self.f_bot, text="Заголовок", borderwidth=5)
        self.headerLabel.grid(row=4, column=0, padx=5, pady=5)
        self.headerBtn = Button(self.f_bot, text="Настроить", borderwidth=2)
        self.headerBtn.grid(row=4, column=1, padx=5, pady=5)

        self.gridLabel = Label(self.f_bot, text="Сетка", borderwidth=5)
        self.gridLabel.grid(row=5, column=0, padx=5, pady=5)
        self.gridBtn = Button(self.f_bot, text="Настроить", borderwidth=2)
        self.gridBtn.grid(row=5, column=1, padx=5, pady=5)

        self.legendLabel = Label(self.f_bot, text="Легенда ", borderwidth=5)
        self.legendLabel.grid(row=7, column=0, padx=5, pady=5)
        self.legendBtn = Button(self.f_bot, text="Настроить", borderwidth=2)
        self.legendBtn.grid(row=7, column=1, padx=5, pady=5)

        self.f_bot.pack(side=RIGHT, fill=Y, padx=[10, 10], pady=[10, 10])


        self.f_down = LabelFrame()

        self.clearBtn = Button(self.f_down, text="Очистить", borderwidth=5, command=self.clear)
        self.clearBtn.grid(row=0, column=0, padx=5, pady=5)

        self.saveBtn = Button(self.f_down, text="Сохранить изображение", borderwidth=5, command=self.save)
        self.saveBtn.grid(row=0, column=1, padx=5, pady=5)

        # self.l9 = Button(self.f_down, text="Сохранить в файл", borderwidth=5)
        # self.l9.grid(row=0, column=2, padx=5, pady=5)
        self. f_down.pack(side=BOTTOM, padx=[10, 10], pady=[10, 10])

        self.fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
        self.ax = self.fig.add_subplot(111)
        self.canvasAgg = FigureCanvasTkAgg(self.fig, master=self)
        self.canvasAgg.draw()
        self.canvas = self.canvasAgg.get_tk_widget()
        self.canvas.pack(fill=BOTH, expand=1)


    line_color = "red"
    line_type = "-"
    line_thick = 1

    def open_lines(self):
        def callback(data):
            self.line_color, self.line_type, self.line_thick = data
        Lines(self, callback)

    x_label_text = ""
    x_label_fontsize = 12
    x_label_color = "black"

    def open_OX(self):
        def callback(data):
            self.x_label_text, self.x_label_fontsize, self.x_label_color = data
            print(data)
        OXname(self, callback)

    Y = []

    def read_from_file(self):
        self.Y = genfromtxt('test.txt', delimiter=';')[0]
        print(self.Y)
        print(self.useFile.get())

    def save(self):
        self.after(100, self.Gen_graph)
        self.canvasAgg.print_figure('1.jpg')

    def clear(self):
        self.ax.clear()
        self.canvasAgg.draw()

    def Gen_graph(self):
        try:
            a = float(self.strA.get())
            b = float(self.strB.get())
            print(str(a) + " " + str(b))

            if (not(self.useFile.get())):
                mystr = self.functionField.get()
                exec('f = lambda x:' + mystr, globals())
                X = linspace(a, b, 350)
                self.Y = [f(x) for x in X]
            else:
                X = linspace(a, b, self.Y.shape[0])

            self.ax.clear()  # очистить графическую область
            self.ax.plot(X, self.Y, color=self.line_color, linestyle=self.line_type, linewidth=self.line_thick)
            self.ax.set_xlabel(self.x_label_text, fontsize=self.x_label_fontsize, color=self.x_label_color)
            self.canvasAgg.draw()  # перерисовать «составной» холст
            return
        except:  # реакция на любую ошибку
            showerror('Ошибка', "Неверное выражение или интервал [a,b].")

    def Gen_graph2(self, event):  # чтобы кнопка отжималась при ошибке
        self.after(100, self.Gen_graph)


if __name__ == "__main__":
    app = App()
    app.mainloop()
