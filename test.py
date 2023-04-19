from tkinter import *
from tkinter import ttk
from numpy import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import customtkinter as ctk

class Header:
    def __init__(self, func):
        self.win = Toplevel()
        self.func = func

        frame = Frame(self.win).pack(padx=5, pady=5)
        self.label = Label(frame, text="Settings Window")
        self.label.pack(padx=20, pady=5)

        self.var = IntVar()
        radio = Radiobutton(frame, text="Option 1", value=1,
                               variable=self.var, command=self.ParentFunc)
        radio.pack(padx=10, pady=5)
        radio2 = Radiobutton(frame, text="Option 2", value=2,
                                variable=self.var, command=self.ParentFunc)
        radio2.pack(padx=10, pady=5)

    def ParentFunc(self):
        self.func(self.var.get())


class Lines(Toplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.geometry("380x325")
        self.title ("Настройка линии")

        line_settings = LabelFrame(text="Настройка элемента линия")

        line_color = Label(line_settings, text="Цвет линии", borderwidth=5)
        line_color_combo = ttk.Combobox(line_settings,
                                        values=["Синий", "Зеленый", "Красный", "Бирюзовый", "Желтый", "Черный"])

        type_line = Label(line_settings, text="Тип линии", borderwidth=5)
        type_line_combo = ttk.Combobox(line_settings, values=["Сплошная", "Штриховая", "Штрих-пунктирная", "Точечная"])

        spinbox_var = StringVar(value=1)
        thick_line = Label(line_settings, text="Толщина линии", borderwidth=5)
        thick_line_spin = Spinbox(line_settings, from_=0, to=10, width=5, textvariable=spinbox_var)

        line_color.grid(row=0, column=0, padx=5, pady=5)
        line_color_combo.grid(row=0, column=1, padx=5, pady=5)
        line_color_combo.current(0)

        type_line.grid(row=1, column=0, padx=5, pady=5)
        type_line_combo.grid(row=1, column=1, padx=5, pady=5)
        type_line_combo.current(0)

        thick_line.grid(row=2, column=0, padx=5, pady=5)
        thick_line_spin.grid(row=2, column=1, padx=5, pady=5)

        line_settings.pack(fill=Y)

        marker_settings = LabelFrame(text="Настройка элемента маркер")

        marker_color = Label(marker_settings, text="Цвет маркера", borderwidth=5)
        marker_color_combo = ttk.Combobox(marker_settings,
                                          values=["Зеленый", "Синий", "Красный", "Бирюзовый", "Желтый", "Черный"])

        type_marker = Label(marker_settings, text="Тип маркера", borderwidth=5)
        type_marker_combo = ttk.Combobox(marker_settings, values=["Точка", "Пиксель", "Окружность", "Треугольник"])

        spinbox_var = StringVar(value=1)
        size_marker = Label(marker_settings, text="Размер маркера", borderwidth=5)
        size_marker_spin = Spinbox(marker_settings, from_=0, to=10, width=5, textvariable=spinbox_var)

        marker_color.grid(row=0, column=0, padx=5, pady=5)
        marker_color_combo.grid(row=0, column=1, padx=5, pady=5)
        marker_color_combo.current(0)

        type_marker.grid(row=1, column=0, padx=5, pady=5)
        type_marker_combo.grid(row=1, column=1, padx=5, pady=5)
        type_marker_combo.current(0)

        size_marker.grid(row=2, column=0, padx=5, pady=5)
        size_marker_spin.grid(row=2, column=1, padx=5, pady=5)

        marker_settings.pack(fill=Y)

        ok = Button(self, text="Применить", borderwidth=2)
        ok.pack(side=TOP, fill=X)

    # def send_data(self):
    #     # Get the value of the entry widget
    #     data = self.entry.get()
    #
    #     # Call the callback function and pass the data
    #     self.callback(data)

class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("995x773")
        self.title("VApp")
        ctk.set_appearance_mode("dark")


        self.f_top = ttk.Label(text="Добавление данных")
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

        fileAdd_button = ttk.Button(self.f_top, text="Добавить файл")
        fileAdd_button.grid(row=2, column=1)



        self.f_top.pack(side=TOP, fill=BOTH, padx=[10, 10], pady=[10, 10])

        fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
        self.ax = fig.add_subplot(111)
        self.canvasAgg = FigureCanvasTkAgg(fig, master=self)
        self.canvasAgg.draw()
        canvas = self.canvasAgg.get_tk_widget()
        canvas.pack(fill=BOTH, expand=1)
        # settings

        self.settings = LabelFrame(text="Настройки")
        ttk.Button(self.settings, text='Заголовок', command=self.open_settings).grid(row=0, column=0)
        ttk.Button(self.settings, text='Легенда', command=self.open_lines).grid(row=0, column=1)
        ttk.Button(self.settings, text='Линии').grid(row=0, column=2)
        ttk.Button(self.settings, text='Подписи по X').grid(row=0, column=3)
        ttk.Button(self.settings, text='Подписи по Y').grid(row=0, column=4)
        self.settings.pack()
        # ttk.Button(self,
        #         text='settings',
        #         command=self.open_settings).pack(expand=True)

    def open_lines(self):
        def callback(data):
            print(data)
        Lines(self, callback)

    def update(self, n):
        self.SettingsValue = n
        print(self.SettingsValue)

    def open_settings(self):
        # window = Window(self)
        # window.grab_set()
        self.settings = Header(self.update)

    def Gen_graph(self, event):
        try:
            mystr = self.function_field.get()
            exec('f = lambda x:' + mystr, globals())
            a = float(self.strA.get())
            b = float(self.strB.get())
            print(str(a)+" "+ str(b))
            X = linspace(a, b, 300)
            Y = [f(x) for x in X]
            self.ax.clear()  # очистить графическую область
            self.ax.plot(X, Y, linewidth=2)
            self.canvasAgg.draw()  # перерисовать «составной» холст
            return
        except:  # реакция на любую ошибку
            showerror('Ошибка', "Неверное выражение или интервал [a,b].")
    def Gen_graph2(self, event):  # чтобы кнопка отжималась при ошибке
        self.after(100, self.Gen_graph, event)




if __name__ == "__main__":
    app = App()
    app.mainloop()