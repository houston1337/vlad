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

        self.f_top = ttk.Label()
        self.f_top.grid_columnconfigure(0, weight=1)
        self.f_top.grid_columnconfigure(1, weight=2)
        self.f_top.grid_columnconfigure(2, weight=1)
        self.f_top.grid_columnconfigure(3, weight=1)

        function_label = Label(self.f_top, width=30, height=2, text="Введите функцию:", anchor='w')
        function_label.grid(row=0, column=0, columnspan=1)

        self.function_field = Entry(self.f_top, width=30)
        self.function_field.bind("<Return>", self.Gen_graph)
        self.function_field.grid(row=0, column=1, columnspan=1)

        interval_start_label = Label(self.f_top, width=30, height=2, text="Начало интервала a:", anchor='w')
        interval_start_label.grid(row=1, column=0)

        self.strA = StringVar()
        self.strA.set(0)
        interval_start_field = Entry(self.f_top, width=5, textvariable=self.strA)
        interval_start_field.bind("<Return>", self.Gen_graph)
        interval_start_field.grid(row=1, column=1)

        interval_end_label = Label(self.f_top, width=15, height=2, text="Конец интервала b:")
        interval_end_label.grid(row=1, column=2)

        self.strB = StringVar()
        self.strB.set(10)
        interval_end_field = Entry(self.f_top, width=3, textvariable=self.strB)
        interval_start_field.bind("<Return>", self.Gen_graph)
        interval_end_field.grid(row=1, column=3)

        build_button = ttk.Button(self.f_top, text="Построить")
        build_button.bind("<Button-1>", self.Gen_graph2)
        build_button.grid(row=0, column=5, ipadx=77, ipady=6, rowspan=3)

        import_label = Label(self.f_top, width=30, height=2, text="Импортировать данные из файла", anchor='w')
        import_label.grid(row=2, column=0, columnspan=1)

        fileAdd_button = ttk.Button(self.f_top, text="Добавить файл", command=self.read_from_file)
        fileAdd_button.grid(row=2, column=1)

        self.use_file = BooleanVar()
        self.use_data_from_file = Checkbutton(self.f_top, text="Использовать данные из файла", variable=self.use_file)
        self.use_data_from_file.grid(row=2, column=2)

        self.f_top.pack(side=TOP, fill=BOTH, padx=[10, 10], pady=[10, 10])

        fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
        self.ax = fig.add_subplot(111)
        self.canvasAgg = FigureCanvasTkAgg(fig, master=self)
        self.canvasAgg.draw()
        canvas = self.canvasAgg.get_tk_widget()
        canvas.pack(fill=BOTH, expand=1)
        # settings

        self.settings = LabelFrame(text="Настройки")
        ttk.Button(self.settings, text='Заголовок').grid(row=0, column=0)
        ttk.Button(self.settings, text='Легенда').grid(row=0, column=1)
        ttk.Button(self.settings, text='Линии', command=self.open_lines).grid(row=0, column=2)
        ttk.Button(self.settings, text='Подписи по X', command=self.open_OX).grid(row=0, column=3)
        ttk.Button(self.settings, text='Подписи по Y').grid(row=0, column=4)
        self.settings.pack()
        # ttk.Button(self,
        #         text='settings',
        #         command=self.open_settings).pack(expand=True)

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
        self.Y = genfromtxt('data/test.txt', delimiter=';')[0]
        print(self.Y)
        print(self.use_file.get())


    def Gen_graph(self):
        try:
            a = float(self.strA.get())
            b = float(self.strB.get())
            print(str(a) + " " + str(b))

            if (not(self.use_file.get())):
                mystr = self.function_field.get()
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
