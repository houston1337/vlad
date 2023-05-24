from tkinter import *
from tkinter import ttk
from colors import COLORS
from titlePositions import POSITION


class Title(Toplevel):
    def __init__(self, master, callback, text='', font_size='12', text_color='black', text_position='center',
                 old_backgrond_color='white'):
        super().__init__(master)
        self.callback = callback
        self.geometry("400x310")
        self.title("Настройка заголовка")

        self.titleFrame = LabelFrame(self, text="Настройка элемента заголовок")

        # Текст
        titleTextLabel = Label(self.titleFrame, width=15, height=2, text="Текст:")
        titleTextLabel.grid(row=0, column=0, padx=5, pady=5)
        self.titleTextField = Entry(self.titleFrame, width=21)
        self.titleTextField.grid(row=0, column=1, padx=5, pady=5)

        self.font_size_value = StringVar(value=font_size)
        textThickLabel = Label(self.titleFrame, text="Размер шрифта", borderwidth=5)
        textThickLabel.grid(row=1, column=0, padx=5, pady=5)
        self.textThickSpin = Spinbox(self.titleFrame, from_=0, to=30, width=5, textvariable=self.font_size_value)
        self.textThickSpin.grid(row=1, column=1, padx=5, pady=5)

        self.text_colors = COLORS
        self.text_colors_label = list(self.text_colors.keys())
        textColorLabel = Label(self.titleFrame, text="Цвет шрифта", borderwidth=5)
        textColorLabel.grid(row=2, column=0, padx=5, pady=5)

        old_text_color_index = list(self.text_colors.values()).index(text_color)
        self.textColorCombo = ttk.Combobox(self.titleFrame, values=self.text_colors_label)
        self.textColorCombo.grid(row=2, column=1, padx=5, pady=5)
        self.textColorCombo.current(old_text_color_index)

        # Выравнивание
        self.text_position = POSITION
        self.text_position_label = list(self.text_position.keys())
        textPositionLabel = Label(self.titleFrame, text="Выравнивание", borderwidth=5)
        textPositionLabel.grid(row=3, column=0, padx=5, pady=5)

        old_text_position_index = list(self.text_position.values()).index(text_position)
        self.textPositionCombo = ttk.Combobox(self.titleFrame, values=self.text_position_label)
        self.textPositionCombo.grid(row=3, column=1, padx=5, pady=5)
        self.textPositionCombo.current(old_text_position_index)

        # Фон

        backgroundColorLabel = Label(self.titleFrame, text="Цвет фона", borderwidth=5)
        backgroundColorLabel.grid(row=4, column=0, padx=5, pady=5)

        old_background_title_color_index = list(self.text_colors.values()).index(old_backgrond_color)
        self.backgroundColorCombo = ttk.Combobox(self.titleFrame, values=self.text_colors_label)
        self.backgroundColorCombo.grid(row=4, column=1, padx=5, pady=5)
        self.backgroundColorCombo.current(old_background_title_color_index)

        self.titleFrame.pack(fill=Y)

        # Кнопки
        self.btnFrame = LabelFrame(self, text="", bd=0)
        ok = ttk.Button(self.btnFrame, text="Применить \nк текущему", command=self.send_data)
        ok.grid(row=0, column=0)
        default = ttk.Button(self.btnFrame, text="Сохранить настройки \nкак стандатные", command=self.set_as_default)
        default.grid(row=0, column=1)
        self.btnFrame.pack(fill=Y, padx=5)

    def set_as_default(self):
        self.master.default_title_text = self.titleTextField.get()
        self.master.default_title_fontsize = int(self.textThickSpin.get())
        self.master.default_title_text_color = self.text_colors[self.textColorCombo.get()]
        self.master.default_title_text_position = self.text_position[self.textPositionCombo.get()]
        self.master.default_title_background_color = self.text_colors[self.backgroundColorCombo.get()]

    def send_data(self):
        title_text = self.titleTextField.get()
        title_fontsize = int(self.textThickSpin.get())
        title_text_color = self.text_colors[self.textColorCombo.get()]
        title_text_position = self.text_position[self.textPositionCombo.get()]
        title_background_color = self.text_colors[self.backgroundColorCombo.get()]

        self.callback([title_text, title_fontsize, title_text_color, title_text_position, title_background_color])
        self.master.gen_graph()
