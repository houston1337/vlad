from tkinter import *
from tkinter import ttk
from colors import COLORS

class Background(Toplevel):

    def __init__(self, master, callback, graph_background_color='white', alpha='1.0'):
        super().__init__(master)
        self.callback = callback
        self.title("Настройка фона")
        self.backgroundFrame = LabelFrame(self, text="Настройка фона")

        self.colors = COLORS
        self.color_label = list(self.colors.keys())


        self.old_graph_background_color = list(self.colors.values()).index(graph_background_color)
        graphBackgroundColor = Label(self.backgroundFrame, text="Фон графика", borderwidth=5)
        graphBackgroundColor.grid(row=0, column=0, padx=5, pady=5)
        self.backgroundColorCombo = ttk.Combobox(self.backgroundFrame, values=self.color_label)
        self.backgroundColorCombo.grid(row=0, column=1, padx=5, pady=5)
        self.backgroundColorCombo.current(self.old_graph_background_color)

        graph_bg_alpha = StringVar(value=alpha)
        graphBgLabel = Label(self.backgroundFrame, text="Прозрачность фона графика", borderwidth=5)
        graphBgLabel.grid(row=1, column=0, padx=5, pady=5)
        self.graphBgSpin = Spinbox(self.backgroundFrame, from_=0, to=1, width=5, textvariable=graph_bg_alpha, increment=.1)
        self.graphBgSpin.grid(row=1, column=1, padx=5, pady=5)


        self.backgroundFrame.pack(fill=Y, padx=5)

        # Кнопки
        self.btnFrame = LabelFrame(self, text="", bd=0)
        ok = ttk.Button(self.btnFrame, text="Применить \nк текущему", command=self.send_data )
        ok.grid(row=0, column=0, ipady=7, ipadx=7)
        default = ttk.Button(self.btnFrame, text="Сохранить настройки \nкак стандатные", command=self.set_as_default)
        default.grid(row=0, column=1, ipady=7, ipadx=7)
        self.btnFrame.pack(fill=Y, padx=5)

    def set_as_default(self):
        self.master.default_background_color = self.colors[self.backgroundColorCombo.get()]
        self.master.background_color_alpha = float(self.graphBgSpin.get())

    def send_data(self):
        background_color = self.colors[self.backgroundColorCombo.get()]
        background_color_alpha = float(self.graphBgSpin.get())
        self.callback([background_color, background_color_alpha])
        self.master.gen_graph()