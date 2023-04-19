from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.geometry("380x135")
root.title ("Настройка фона")



line_settings = LabelFrame(text="Настройка элемента фон")

line_color = Label(line_settings, text="Цвет фона", borderwidth=5)
line_color_combo = ttk.Combobox(line_settings, values=[ "Синий",  "Зеленый",   "Красный",   "Бирюзовый",   "Желтый",   "Черный"])

type_line = Label (line_settings, text="Прозрачность", borderwidth=5) 
type_line_combo = ttk.Combobox(line_settings, values=[ "0",  "25",   "50",   "75" ,  "100"])





line_color.grid(row=0, column=0, padx=5, pady=5)
line_color_combo.grid(row=0, column=1, padx=5, pady=5)
line_color_combo.current(0)

type_line.grid(row=1, column=0, padx=5, pady=5)
type_line_combo.grid(row=1, column=1, padx=5, pady=5)
type_line_combo.current(0)

line_settings.pack(fill=Y)  






ok = Button (root, text="Применить", borderwidth=2)
ok.pack(side=TOP,fill=X)


root.mainloop()