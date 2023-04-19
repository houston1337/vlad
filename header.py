from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.geometry("400x310")
root.title ("Настройка заголовка")



line_settings = LabelFrame(text="Настройка элемента заголовок")


l1 = Label(line_settings, width=15, height=2,text="Текст:")
l4 = Entry (line_settings, width=21)

spinbox_var = StringVar(value=1)
thick_line = Label (line_settings, text="Размер шрифта", borderwidth=5)
thick_line_spin = Spinbox(line_settings, from_= 0, to = 10,width=5, textvariable=spinbox_var)


type_line = Label (line_settings, text="Цвет текста", borderwidth=5) 
type_line_combo = ttk.Combobox(line_settings, values=[ "Черный",  "Зеленый",   "Красный",   "Синий",   "Белый"])


line_color = Label(line_settings, text="Выравнивание", borderwidth=5)
line_color_combo = ttk.Combobox(line_settings, values=[ "По левому краю",  "Центр",   "По правому краю"])


type_line1 = Label (line_settings, text="Цвет фона", borderwidth=5) 
type_line_combo1 = ttk.Combobox(line_settings, values=[ "Белый",  "Зеленый",   "Красный",   "Черный"])

type_line2= Label (line_settings, text="Прозрачность фона", borderwidth=5) 
type_line_combo2 = ttk.Combobox(line_settings, values=[ "0",  "25",   "50",   "75" ,  "100"])




l1.grid(row=0, column=0, padx=5, pady=5)
l4.grid(row=0, column=1, padx=5, pady=5)

thick_line.grid(row=1, column=0, padx=5, pady=5)
thick_line_spin.grid(row=1, column=1, padx=5, pady=5)

type_line.grid(row=2, column=0, padx=5, pady=5)
type_line_combo.grid(row=2, column=1, padx=5, pady=5)
type_line_combo.current(0)


line_color.grid(row=3, column=0, padx=5, pady=5)
line_color_combo.grid(row=3, column=1, padx=5, pady=5)
line_color_combo.current(0)

type_line1.grid(row=4, column=0, padx=5, pady=5)
type_line_combo1.grid(row=4, column=1, padx=5, pady=5)
type_line_combo1.current(0)


type_line2.grid(row=5, column=0, padx=5, pady=5)
type_line_combo2.grid(row=5, column=1, padx=5, pady=5)
type_line_combo2.current(0)





line_settings.pack(fill=Y)  




ok = Button (root, text="Применить", borderwidth=2)
ok.pack(side=TOP,fill=X)


root.mainloop()