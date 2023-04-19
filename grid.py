from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.geometry("380x325")
root.title ("Настройка сетки")



line_settings = LabelFrame(text="Настройка сетки по оси X")

line_color = Label(line_settings, text="Цвет сетки", borderwidth=5)
line_color_combo = ttk.Combobox(line_settings, values=[ "Синий",  "Зеленый",   "Красный",   "Бирюзовый",   "Желтый",   "Черный"])

type_line = Label (line_settings, text="Начертание", borderwidth=5) 
type_line_combo = ttk.Combobox(line_settings, values=[ "Сплошная",  "Штриховая",   "Штрих-пунктирная",   "Точечная"])

spinbox_var = StringVar(value=1)
thick_line = Label (line_settings, text="Толщина сетки", borderwidth=5)
thick_line_spin = Spinbox(line_settings, from_= 0, to = 10,width=5, textvariable=spinbox_var)



line_color.grid(row=0, column=0, padx=5, pady=5)
line_color_combo.grid(row=0, column=1, padx=5, pady=5)
line_color_combo.current(0)

type_line.grid(row=1, column=0, padx=5, pady=5)
type_line_combo.grid(row=1, column=1, padx=5, pady=5)
type_line_combo.current(0)

thick_line.grid(row=2, column=0, padx=5, pady=5)
thick_line_spin.grid(row=2, column=1, padx=5, pady=5)


line_settings.pack(fill=Y)  




marker_settings = LabelFrame(text="Настройка сетки по оси Y")



marker_color = Label(marker_settings, text="Цвет сетки", borderwidth=5)
marker_color_combo = ttk.Combobox(marker_settings, values=["Зеленый",  "Синий",   "Красный",   "Бирюзовый",   "Желтый",   "Черный"])

type_marker = Label (marker_settings, text="Начертание", borderwidth=5) 
type_marker_combo = ttk.Combobox(marker_settings, values=[ "Сплошная",  "Штриховая",   "Штрих-пунктирная",   "Точечная"])

spinbox_var = StringVar(value=1)
size_marker = Label (marker_settings, text="Толщина сетки", borderwidth=5)
size_marker_spin = Spinbox(marker_settings, from_= 0, to = 10,width=5, textvariable=spinbox_var)


marker_color.grid(row=0, column=0, padx=5, pady=5)
marker_color_combo.grid(row=0, column=1, padx=5, pady=5)
marker_color_combo.current(0)

type_marker.grid(row=1, column=0, padx=5, pady=5)
type_marker_combo.grid(row=1, column=1, padx=5, pady=5)
type_marker_combo.current(0)

size_marker.grid(row=2, column=0, padx=5, pady=5)
size_marker_spin.grid(row=2, column=1, padx=5, pady=5)

marker_settings.pack(fill=Y)  

ok = Button (root, text="Применить", borderwidth=2)
ok.pack(side=TOP,fill=X)


root.mainloop()