from tkinter import *
from tkinter import ttk
from location import LOCATION


class Legend(Toplevel):
    def __init__(self, master, callback, text='', location='best', font_size='12', shadow=False, is_show_legend=False):
        super().__init__(master)
        self.callback = callback
        self.title("Настройка легенды")

        settingsFrame = LabelFrame(self, text="Настройка легенды")

        # Текст который будет написан в легенде
        self.strText = StringVar()
        self.strText.set(text)
        legendLabel = Label(settingsFrame, width=15, height=2, text="Текст:")
        legendLabel.grid(row=0, column=0, padx=5, pady=5)
        self.legendField = Entry(settingsFrame, width=21, textvariable=self.strText)
        self.legendField.grid(row=0, column=1, padx=5, pady=5)

        # Позиционирование легенды
        self.legend_location = LOCATION
        self.legend_location_labels = list(self.legend_location.keys())
        self.old_location = list(self.legend_location.values()).index(location)
        legendLocationLabel = Label(settingsFrame, text="Положение легенды", borderwidth=5)
        legendLocationLabel.grid(row=1, column=0, padx=5, pady=5)
        self.legendLocationCombo = ttk.Combobox(settingsFrame, values=self.legend_location_labels)
        self.legendLocationCombo.grid(row=1, column=1, padx=5, pady=5)
        self.legendLocationCombo.current(0)

        # Тень легенды
        self.isShadow = BooleanVar()
        self.isShadow.set(shadow)
        legendShadowCheck = ttk.Checkbutton(settingsFrame, text="Тень легенды", variable=self.isShadow)
        legendShadowCheck.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        # Размер шрифта легенды
        font_size_value = StringVar(value=font_size)
        fontSizeLabel = Label(settingsFrame, text="Размер шрифта", borderwidth=5)
        fontSizeLabel.grid(row=3, column=0, padx=5, pady=5)
        self.fontSizeSpin = Spinbox(settingsFrame, from_=0, to=30, width=5, textvariable=font_size_value)
        self.fontSizeSpin.grid(row=3, column=1, padx=5, pady=5)

        # Показывать/Скрывать легеду
        self.isShowLegend = BooleanVar()
        self.isShowLegend.set(is_show_legend)
        self.isShowLegendCheck = ttk.Checkbutton(settingsFrame, text="Показать легенду", variable=self.isShowLegend)
        self.isShowLegendCheck.grid(row=4, column=0, columnspan=2)

        settingsFrame.pack(fill=Y, padx=5)

        # Кнопки
        self.btnFrame = LabelFrame(self, text="", bd=0)
        ok = ttk.Button(self.btnFrame, text="Применить \nк текущему", command=self.send_data)
        ok.grid(row=0, column=0)
        default = ttk.Button(self.btnFrame, text="Сохранить настройки \nкак стандатные", command=self.set_as_default)
        default.grid(row=0, column=1)
        self.btnFrame.pack(fill=Y, padx=5)

    def set_as_default(self):
        self.master.default_legend = self.legendField.get()
        self.master.default_legend_location = self.legend_location[self.legendLocationCombo.get()]
        self.master.default_legend_fontsize = self.thickLineSpin.get()
        self.master.default_legend_shadow = self.isShadow.get()
        self.master.default_is_show_legend = self.isShowLegend.get()

    def send_data(self):
        legend = self.legendField.get()
        legend_location = self.legend_location[self.legendLocationCombo.get()]
        legend_fontsize = self.fontSizeSpin.get()
        legend_shadow = self.isShadow.get()
        is_show_legend = self.isShowLegend.get()

        self.callback([legend, legend_location, legend_fontsize, legend_shadow, is_show_legend])
        self.master.gen_graph()
