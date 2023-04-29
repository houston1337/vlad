from tkinter import *
from tkinter import ttk
from location import LOCATION


class Legend(Toplevel):
    def __init__(self, master, callback, text='', location='best', font_size=12, shadow=False):
        super().__init__(master)
        self.callback = callback
        self.title("Настройка легенды")

        settingsFrame = LabelFrame(self, text="Настройка легенды")

        # текст который будет написан в легенде
        self.strText = StringVar()
        self.strText.set(text)
        legendLabel = Label(settingsFrame, width=15, height=2, text="Текст:")
        legendLabel.grid(row=0, column=0, padx=5, pady=5)
        self.legendField = Entry(settingsFrame, width=21, textvariable=self.strText)
        self.legendField.grid(row=0, column=1, padx=5, pady=5)

        self.legend_location = LOCATION
        self.legend_location_labels = list(self.legend_location.keys())
        self.old_location = list(self.legend_location.values()).index(location)
        legendLocationLabel = Label(settingsFrame, text="Положение легенды", borderwidth=5)
        legendLocationLabel.grid(row=1, column=0, padx=5, pady=5)
        self.legendLocationCombo = ttk.Combobox(settingsFrame, values=self.legend_location_labels)
        self.legendLocationCombo.grid(row=1, column=1, padx=5, pady=5)
        self.legendLocationCombo.current(0)

        self.isShadow = BooleanVar()
        self.isShadow.set(shadow)
        legendShadowCheck = ttk.Checkbutton(settingsFrame, text="Тень легенды", variable=self.isShadow)
        legendShadowCheck.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        font_size_value = StringVar(value=font_size)
        fontSizeLabel = Label(settingsFrame, text="Размер шрифта", borderwidth=5)
        fontSizeLabel.grid(row=3, column=0, padx=5, pady=5)
        self.fontSizeSpin = Spinbox(settingsFrame, from_=0, to=30, width=5, textvariable=font_size_value)
        self.fontSizeSpin.grid(row=3, column=1, padx=5, pady=5)

        settingsFrame.pack(fill=Y, padx=5)

        ok = ttk.Button(self, text="Применить", command=self.send_data)
        ok.pack(side=TOP)

    def send_data(self):
        legend = self.legendField.get()
        legend_location = self.legend_location[self.legendLocationCombo.get()]
        legend_fontsize = self.fontSizeSpin.get()
        legend_shadow = self.isShadow.get()

        self.callback([legend, legend_location, legend_fontsize, legend_shadow])
        self.master.gen_graph()
