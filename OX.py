from tkinter import *
from tkinter import ttk
from colors import color_Mapping


class OXname(Toplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.geometry("380x285")
        self.title("Настройка оси X")

        self.line_settings = LabelFrame(self, text="Настройка подписи")

        self.l1 = Label(self.line_settings, width=15, height=2, text="Текст:")
        self.l4 = Entry(self.line_settings, width=21)

        # Цвет
        self.text_colors = color_Mapping
        self.text_colors_label = list(self.text_colors.keys())
        self.line_color = Label(self.line_settings, text="Цвет шрифта", borderwidth=5)

        self.line_color_combo = ttk.Combobox(self.line_settings, values=self.text_colors_label)

        self.spinbox_var = StringVar(value=12)
        self.thick_line = Label(self.line_settings, text="Размер шрифта", borderwidth=5)
        self.thick_line_spin = Spinbox(self.line_settings, from_=0, to=30, width=5, textvariable=self.spinbox_var)

        self.l1.grid(row=0, column=0, padx=5, pady=5)
        self.l4.grid(row=0, column=1, padx=5, pady=5)

        self.line_color.grid(row=1, column=0, padx=5, pady=5)
        self.line_color_combo.grid(row=1, column=1, padx=5, pady=5)
        self.line_color_combo.current(0)

        self.thick_line.grid(row=2, column=0, padx=5, pady=5)
        self.thick_line_spin.grid(row=2, column=1, padx=5, pady=5)

        self.line_settings.pack(fill=Y)

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
        ok.pack(side=TOP, fill=X)

    def send_data(self):
        text = self.l4.get()
        font_size = self.thick_line_spin.get()
        color = color_Mapping[self.line_color_combo.get()]
        self.callback([text, font_size, color])
        self.master.Gen_graph()