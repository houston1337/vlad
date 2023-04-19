from tkinter import *
from tkinter import ttk
from colors import color_Mapping

class Lines(Toplevel):

    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback

        self.geometry("380x325")
        self.title("Настройка линии")

        self.line_settings = LabelFrame(self, text="Настройка элемента линия")

        # Цвет
        self.line_color_Mapping = color_Mapping
        self.line_color_label = list(self.line_color_Mapping.keys())

        line_color = Label(self.line_settings, text="Цвет линии", borderwidth=5)
        self.line_color_combo = ttk.Combobox(self.line_settings, values=self.line_color_label)

        # Тип
        self.line_type_Mapping = {"Сплошная": "-", "Штриховая": "--", "Штрих-пунктирная": "-.", "Точечная": ":"}
        self.line_type_label = list(self.line_type_Mapping.keys())

        self.type_line = Label(self.line_settings, text="Тип линии", borderwidth=5)
        self.type_line_combo = ttk.Combobox(self.line_settings, values=self.line_type_label)

        # Толщина
        spinbox_var = StringVar(value=1)
        self.thick_line = Label(self.line_settings, text="Толщина линии", borderwidth=5)
        self.thick_line_spin = Spinbox(self.line_settings, from_=0, to=10, width=5, textvariable=spinbox_var)

        line_color.grid(row=0, column=0, padx=5, pady=5)
        self.line_color_combo.grid(row=0, column=1, padx=5, pady=5)
        self.line_color_combo.current(0)

        self.type_line.grid(row=1, column=0, padx=5, pady=5)
        self.type_line_combo.grid(row=1, column=1, padx=5, pady=5)
        self.type_line_combo.current(0)

        self.thick_line.grid(row=2, column=0, padx=5, pady=5)
        self.thick_line_spin.grid(row=2, column=1, padx=5, pady=5)

        self.line_settings.pack(fill=Y)

        marker_settings = LabelFrame(self, text="Настройка элемента маркер")

        marker_color = Label(marker_settings, text="Цвет маркера", borderwidth=5)
        marker_color_combo = ttk.Combobox(marker_settings,
                                          values=self.line_color_label)

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

        ok = Button(self, text="Применить", borderwidth=1, command=self.send_data)
        ok.pack(side=TOP, fill=X)

    def send_data(self):
        # Get the value of the entry widget

        line_color = self.line_color_Mapping[self.line_color_combo.get()]
        line_type = self.line_type_Mapping[self.type_line_combo.get()]
        line_thick = self.thick_line_spin.get()
        # Call the callback function and pass the data
        self.callback([line_color, line_type, line_thick])
        self.master.Gen_graph()