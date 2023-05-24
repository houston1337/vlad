from tkinter import *
from tkinter import ttk
from colors import COLORS


class Oy(Toplevel):
    def __init__(self, master, callback, text='', font_size='12', text_color='black', major_var='1', minor_var='1'):
        super().__init__(master)
        self.callback = callback
        self.geometry("380x285")
        self.title("Настройка оси Y")

        self.settingsFrame = LabelFrame(self, text="Настройка подписи")

        self.strText = StringVar()
        self.strText.set(text)
        textLabel = Label(self.settingsFrame, width=15, height=2, text="Текст:")
        textLabel.grid(row=0, column=0, padx=5, pady=5)
        self.textField = Entry(self.settingsFrame, width=21, textvariable=self.strText)
        self.textField.grid(row=0, column=1, padx=5, pady=5)

        # Цвет
        self.text_colors = COLORS
        self.text_colors_label = list(self.text_colors.keys())
        textColorLabel = Label(self.settingsFrame, text="Цвет шрифта", borderwidth=5)
        textColorLabel.grid(row=1, column=0, padx=5, pady=5)

        old_text_color_index = list(self.text_colors.values()).index(text_color)
        self.textColorCombo = ttk.Combobox(self.settingsFrame, values=self.text_colors_label)
        self.textColorCombo.grid(row=1, column=1, padx=5, pady=5)
        self.textColorCombo.current(old_text_color_index)

        # Размер шрифта
        self.font_size_value = StringVar(value=font_size)
        textThickLabel = Label(self.settingsFrame, text="Размер шрифта", borderwidth=5)
        textThickLabel.grid(row=2, column=0, padx=5, pady=5)
        self.textThickSpin = Spinbox(self.settingsFrame, from_=0, to=30, width=5, textvariable=self.font_size_value)
        self.textThickSpin.grid(row=2, column=1, padx=5, pady=5)

        self.settingsFrame.pack(fill=Y)


        # Деления
        self.locatorFrame = LabelFrame(self, text="Настройка делений")

        # Основные
        self.major_spinbox_var = StringVar(value=major_var)
        majorLabel = Label(self.locatorFrame, text="Интервал основных делений", borderwidth=5)
        majorLabel.grid(row=0, column=0, padx=5, pady=5)
        self.majorSpin = Spinbox(self.locatorFrame, from_=0, to=100, width=5, textvariable=self.major_spinbox_var,
                                 increment=.1)
        self.majorSpin.grid(row=0, column=1, padx=5, pady=5)

        # Вспомогательные
        self.minor_spinbox_var = StringVar(value=minor_var)
        minorLabel = Label(self.locatorFrame, text="Интервал вспомогательных делений", borderwidth=5)
        minorLabel.grid(row=1, column=0, padx=5, pady=5)
        self.minorSpin = Spinbox(self.locatorFrame, from_=0, to=10, width=5, textvariable=self.minor_spinbox_var,
                                 increment=.1)
        self.minorSpin.grid(row=1, column=1, padx=5, pady=5)
        self.locatorFrame.pack()

        # Кнопки
        self.btnFrame = LabelFrame(self, text="", bd=0)
        ok = ttk.Button(self.btnFrame, text="Применить \nк текущему", command=self.send_data)
        ok.grid(row=0, column=0)
        default = ttk.Button(self.btnFrame, text="Сохранить настройки \nкак стандатные", command=self.set_as_default)
        default.grid(row=0, column=1)
        self.btnFrame.pack(fill=Y, padx=5)

    def set_as_default(self):
        self.master.default_x_label_text = self.textField.get()
        self.master.default_x_label_fontsize = self.textThickSpin.get()
        self.master.default_x_label_color = self.text_colors[self.textColorCombo.get()]
        self.master.default_x_major_locator = float(self.majorSpin.get())
        self.master.default_x_minor_locator = float(self.minorSpin.get())

    def send_data(self):
        y_label_text = self.textField.get()
        y_label_fontsize = self.textThickSpin.get()
        y_label_color = self.text_colors[self.textColorCombo.get()]
        y_major_locator = float(self.majorSpin.get())
        y_minor_locator = float(self.minorSpin.get())
        self.callback([y_label_text, y_label_fontsize, y_label_color, y_major_locator, y_minor_locator])
        self.master.gen_graph()
