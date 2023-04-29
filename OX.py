from tkinter import *
from tkinter import ttk
from colors import COLORS


class OXname(Toplevel):
    def __init__(self, master, callback, text='', font_size=12, text_color='black'):
        super().__init__(master)
        self.callback = callback
        self.geometry("380x285")
        self.title("Настройка оси X")

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

        marker_settings = LabelFrame(self, text="Настройка делений")

        spinbox_var = StringVar(value=10)
        thick_line1 = Label(marker_settings, text="Интервал основных делений", borderwidth=5)
        thick_line_spin1 = Spinbox(marker_settings, from_=0, to=10, width=5, textvariable=spinbox_var)

        spinbox_var = StringVar(value=1)
        thick_line = Label(marker_settings, text="Интервал вспомогательных делений", borderwidth=5)
        thick_line_spin = Spinbox(marker_settings, from_=0, to=10, width=5, textvariable=spinbox_var)

        thick_line1.grid(row=0, column=0, padx=5, pady=5)
        thick_line_spin1.grid(row=0, column=1, padx=5, pady=5)

        thick_line.grid(row=1, column=0, padx=5, pady=5)
        thick_line_spin.grid(row=1, column=1, padx=5, pady=5)

        marker_settings.pack(fill=Y)
        ok = Button(self, text="Применить", borderwidth=2, command=self.send_data)
        ok.pack(side=TOP)

    def send_data(self):
        text = self.textField.get()
        font_size = self.textThickSpin.get()
        color = self.text_colors[self.textColorCombo.get()]
        self.callback([text, font_size, color])
        self.master.gen_graph()
