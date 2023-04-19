from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.geometry("380x285")
root.title ("Настройка оси X")



line_settings = LabelFrame(text="Настройка подписи")


l1 = Label(line_settings, width=15, height=2,text="Текст:")
l4 = Entry (line_settings, width=21)


line_color = Label(line_settings, text="Цвет шрифта", borderwidth=5)
line_color_combo = ttk.Combobox(line_settings, values=[ "Синий",  "Зеленый",   "Красный",   "Бирюзовый",   "Желтый",   "Черный"])


spinbox_var = StringVar(value=1)
thick_line = Label (line_settings, text="Размер шрифта", borderwidth=5)
thick_line_spin = Spinbox(line_settings, from_= 0, to = 10,width=5, textvariable=spinbox_var)



l1.grid(row=0, column=0, padx=5, pady=5)
l4.grid(row=0, column=1, padx=5, pady=5)

line_color.grid(row=1, column=0, padx=5, pady=5)
line_color_combo.grid(row=1, column=1, padx=5, pady=5)
line_color_combo.current(0)



thick_line.grid(row=2, column=0, padx=5, pady=5)
thick_line_spin.grid(row=2, column=1, padx=5, pady=5)


line_settings.pack(fill=Y)  


marker_settings = LabelFrame(text="Настройка делений")

spinbox_var = StringVar(value=10)
thick_line1 = Label (marker_settings, text="Интервал основных делений", borderwidth=5)
thick_line_spin1 = Spinbox(marker_settings, from_= 0, to = 10,width=5, textvariable=spinbox_var)

spinbox_var = StringVar(value=1)
thick_line = Label (marker_settings, text="Интервал вспомогательных делений", borderwidth=5)
thick_line_spin = Spinbox(marker_settings, from_= 0, to = 10,width=5, textvariable=spinbox_var)



thick_line1.grid(row=0, column=0, padx=5, pady=5)
thick_line_spin1.grid(row=0, column=1, padx=5, pady=5)


thick_line.grid(row=1, column=0, padx=5, pady=5)
thick_line_spin.grid(row=1, column=1, padx=5, pady=5)


marker_settings.pack(fill=Y)  






ok = Button (root, text="Применить", borderwidth=2)
ok.pack(side=TOP,fill=X)


root.mainloop()