from tkinter import *
from tkinter import ttk
from colors import COLORS
from lineType import LINE_TYPE


class Grid(Toplevel):
    def __init__(self, master, callback, grid_color='grey', grid_type=' ', grid_thickness='0.1', axis='both'):
        super().__init__(master)
        self.callback = callback

        self.title("Настройка сетки")
        settingsFrame = LabelFrame(self, text="Настройка сетки")

        # Цвет линии
        self.line_color_Mapping = COLORS
        self.line_color_label = list(self.line_color_Mapping.keys())
        lineColor = Label(settingsFrame, text="Цвет сетки", borderwidth=5)
        lineColor.grid(row=0, column=0, padx=5, pady=5)
        old_color_index = list(self.line_color_Mapping.values()).index(grid_color)
        self.lineColorCombo = ttk.Combobox(settingsFrame, values=self.line_color_label)
        self.lineColorCombo.grid(row=0, column=1, padx=5, pady=5)
        self.lineColorCombo.current(old_color_index)

        # Тип линии
        self.line_type_Mapping = LINE_TYPE
        self.line_type_label = list(self.line_type_Mapping.keys())
        old_type_index = list(self.line_type_Mapping.values()).index(grid_type)
        typeLine = Label(settingsFrame, text="Начертание", borderwidth=5)
        typeLine.grid(row=1, column=0, padx=5, pady=5)
        self.typeLineCombo = ttk.Combobox(settingsFrame, values=self.line_type_label)
        self.typeLineCombo.current(old_type_index)
        self.typeLineCombo.grid(row=1, column=1, padx=5, pady=5)

        # Толщина сетки
        thickness = StringVar(value=grid_thickness)
        thickLineLabel = Label(settingsFrame, text="Толщина сетки", borderwidth=5)
        thickLineLabel.grid(row=2, column=0, padx=5, pady=5)
        self.thickLineSpin = Spinbox(settingsFrame, from_=0, to=10, width=5, increment=0.1, textvariable=thickness)
        self.thickLineSpin.grid(row=2, column=1, padx=5, pady=5)

        settingsFrame.pack(fill=Y, padx=5)

        self.isXOn = BooleanVar()
        self.xGrid = ttk.Checkbutton(settingsFrame, text="Включить сетку для оси X", variable=self.isXOn)
        self.xGrid.grid(row=3, column=0, columnspan=2, )

        self.isYOn = BooleanVar()
        self.yGrid = ttk.Checkbutton(settingsFrame, text="Включить сетку для оси Y", variable=self.isYOn)
        self.yGrid.grid(row=4, column=0, columnspan=2, )

        if (axis == 'both'):
            self.isXOn.set(True)
            self.isYOn.set(True)
        elif (axis == 'x'):
            self.isXOn.set(True)
            self.isYOn.set(False)
        elif (axis == 'y'):
            self.isXOn.set(False)
            self.isYOn.set(True)

        # Кнопки
        self.btnFrame = LabelFrame(self, text="", bd=0)
        ok = ttk.Button(self.btnFrame, text="Применить \nк текущему", command=self.send_data)
        ok.grid(row=0, column=0)
        default = ttk.Button(self.btnFrame, text="Сохранить настройки \nкак стандатные",
                             command=self.set_as_default)
        default.grid(row=0, column=1)
        self.btnFrame.pack(fill=Y, padx=5)

    def set_as_default(self):
        if (self.isXOn.get() and self.isYOn.get()):
            self.master.default_grid_axis = 'both'
        elif (self.isXOn.get() and not (self.isYOn.get())):
            self.master.default_grid_axis = 'x'
        elif (not (self.isXOn.get()) and self.isYOn.get()):
            self.master.default_grid_axis = 'y'
        elif (not (self.isXOn.get()) and not (self.isYOn.get())):
            self.master.default_grid_axis = 'both'
            none = list(self.line_type_Mapping.values()).index(" ")
            self.typeLineCombo.current(none)

        self.master.default_grid_color = self.line_color_Mapping[self.lineColorCombo.get()]
        self.master.default_grid_type = self.line_type_Mapping[self.typeLineCombo.get()]
        self.master.default_grid_thickness = self.thickLineSpin.get()


    def send_data(self):
        if (self.isXOn.get() and self.isYOn.get()):
            grid_axis = 'both'
        elif (self.isXOn.get() and not (self.isYOn.get())):
            grid_axis = 'x'
        elif (not (self.isXOn.get()) and self.isYOn.get()):
            grid_axis = 'y'
        elif (not (self.isXOn.get()) and not (self.isYOn.get())):
            grid_axis = 'both'
            none = list(self.line_type_Mapping.values()).index(" ")
            self.typeLineCombo.current(none)

        grid_color = self.line_color_Mapping[self.lineColorCombo.get()]
        grid_type = self.line_type_Mapping[self.typeLineCombo.get()]
        lineThickness = self.thickLineSpin.get()

        self.callback([grid_color, grid_type, lineThickness, grid_axis])
        self.master.gen_graph()
