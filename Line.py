from tkinter import *
from tkinter import ttk
from colors import COLORS
from lineType import LINE_TYPE
from markerType import MARKER_TYPE


class Lines(Toplevel):

    def __init__(self, master, callback, line_color='black', line_type='-', line_thickness=1, marker_color='black',
                 marker_type='', marker_size=1):
        super().__init__(master)
        self.callback = callback

        #
        # Линия
        #
        self.title("Настройка линии")
        self.settingsFrameLine = LabelFrame(self, text="Настройка элемента линия")

        # Цвет
        self.line_color_Mapping = COLORS
        self.line_color_label = list(self.line_color_Mapping.keys())
        self.old_line_color = list(self.line_color_Mapping.values()).index(line_color)

        lineColor = Label(self.settingsFrameLine, text="Цвет линии", borderwidth=5)
        lineColor.grid(row=0, column=0, padx=5, pady=5)
        self.lineColorCombo = ttk.Combobox(self.settingsFrameLine, values=self.line_color_label)
        self.lineColorCombo.grid(row=0, column=1, padx=5, pady=5)
        self.lineColorCombo.current(self.old_line_color)

        # Тип
        self.line_type_Mapping = LINE_TYPE
        self.line_type_label = list(self.line_type_Mapping.keys())
        self.old_line_type = list(self.line_type_Mapping.values()).index(line_type)
        self.typeLineLabel = Label(self.settingsFrameLine, text="Тип линии", borderwidth=5)
        self.typeLineLabel.grid(row=1, column=0, padx=5, pady=5)
        self.typeLineCombo = ttk.Combobox(self.settingsFrameLine, values=self.line_type_label)
        self.typeLineCombo.grid(row=1, column=1, padx=5, pady=5)
        self.typeLineCombo.current(self.old_line_type)

        # Толщина
        spinbox_var = StringVar(value=line_thickness)
        self.thickLineLabel = Label(self.settingsFrameLine, text="Толщина линии", borderwidth=5)
        self.thickLineLabel.grid(row=2, column=0, padx=5, pady=5)
        self.thickLineSpin = Spinbox(self.settingsFrameLine, from_=0, to=10, width=5, textvariable=spinbox_var)
        self.thickLineSpin.grid(row=2, column=1, padx=5, pady=5)

        self.settingsFrameLine.pack(fill=Y, padx=5)

        #
        # Маркеры
        #
        settingsFrameMarker = LabelFrame(self, text="Настройка элемента маркер")

        # Цвет маркера
        self.old_marker_color = list(self.line_color_Mapping.values()).index(marker_color)
        markerColorLabel = Label(settingsFrameMarker, text="Цвет маркера", borderwidth=5)
        markerColorLabel.grid(row=0, column=0, padx=5, pady=5)
        self.markerColorCombo = ttk.Combobox(settingsFrameMarker, values=self.line_color_label)
        self.markerColorCombo.grid(row=0, column=1, padx=5, pady=5)
        self.markerColorCombo.current(self.old_marker_color)

        # Тип маркера
        self.marker_type = MARKER_TYPE
        self.marker_label = list(self.marker_type.keys())
        self.old_marker_type = list(self.marker_type.values()).index(marker_type)

        typeMarkerLabel = Label(settingsFrameMarker, text="Тип маркера", borderwidth=5)
        typeMarkerLabel.grid(row=1, column=0, padx=5, pady=5)
        self.typeMarkerCombo = ttk.Combobox(settingsFrameMarker, values=self.marker_label)
        self.typeMarkerCombo.grid(row=1, column=1, padx=5, pady=5)
        self.typeMarkerCombo.current(self.old_marker_type)

        # Размер маркера
        markerSizeLabel = Label(settingsFrameMarker, text="Размер маркера", borderwidth=5)
        markerSizeLabel.grid(row=2, column=0, padx=5, pady=5)
        self.markerSize = StringVar(value=marker_size)
        self.markerSizeSpin = Spinbox(settingsFrameMarker, from_=0, to=10, width=5, textvariable=self.markerSize)
        self.markerSizeSpin.grid(row=2, column=1, padx=5, pady=5)


        settingsFrameMarker.pack(fill=Y, padx=5)

        self.btnFrame = LabelFrame(self, text="", bd=0)
        ok = ttk.Button(self.btnFrame, text="Применить \nк текущему", command=self.send_data)
        ok.grid(row=0, column=0)
        default = ttk.Button(self.btnFrame, text="Сохранить настройки \nкак стандатные", command=self.set_as_default)
        default.grid(row=0, column=1)
        self.btnFrame.pack(fill=Y, padx=5)

    def set_as_default(self):
        self.master.default_color = self.line_color_Mapping[self.lineColorCombo.get()]
        self.master.default_line_type = self.line_type_Mapping[self.typeLineCombo.get()]
        self.master.default_line_thick = self.thickLineSpin.get()

        self.master.default_marker_color = self.line_color_Mapping[self.markerColorCombo.get()]
        self.master.default_marker_type = self.marker_type[self.typeMarkerCombo.get()]
        self.master.default_marker_size = self.markerSizeSpin.get()

    def send_data(self):
        line_color = self.line_color_Mapping[self.lineColorCombo.get()]
        line_type = self.line_type_Mapping[self.typeLineCombo.get()]
        line_thick = self.thickLineSpin.get()

        markerColor = self.line_color_Mapping[self.markerColorCombo.get()]
        markerType = self.marker_type[self.typeMarkerCombo.get()]
        markerSize = self.markerSizeSpin.get()

        self.callback([line_color, line_type, line_thick, markerColor, markerType, markerSize])
        self.master.gen_graph()
