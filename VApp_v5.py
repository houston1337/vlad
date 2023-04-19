from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.geometry("995x773")
root.title ("VApp")


#добавление канвы для построения графиков 
def Gen_graph () :
    fig = Figure (figsize=(10, 10), dpi=65) # Figure Size
    plot1 = fig.add_subplot (111)
    plot1.plot ([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5]) # Ploting Graph
    canvas1 = FigureCanvasTkAgg (fig, master=canvas)
    
    # Встраивание в холст
    canvas1.draw()
    canvas1.get_tk_widget().pack(padx=1, pady=1)
  
    canvas1.get_tk_widget().pack(side=RIGHT, fill=BOTH)
    

    
#окно ввода функции (объявление, построение)      
         
f_top = LabelFrame(text="Добавление данных")

l1 = Label(f_top, width=15, height=2,text="Введите функцию:")
l2 = Button (f_top, text="Построить", borderwidth=5, command=Gen_graph)

l_1 = Label(f_top, width=15, height=2,text="Начало интервала a:")
l_4 = Entry (f_top, width=3)

l_11 = Label(f_top, width=15, height=2,text="Конец интервала b:")
l_44 = Entry (f_top, width=3)

l_3 = Label(f_top, width=25, height=2,text="Импортировать данные из файла")
l3 = Button (f_top, text="Добавить файл", borderwidth=5)
l4 = Entry (f_top, width=47)


l1.grid(row=0, column=0, columnspan=1)
l4.grid(row=0, column=2, columnspan=3)

l2.grid(row=0, column=5,ipadx=77, ipady=6,rowspan=3)
l_1.grid(row=1, column=0)
l_4.grid(row=1, column=1)
l_11.grid(row=1, column=2)
l_44.grid(row=1, column=3)

l_3.grid(row=2, column=0, columnspan=1)
l3.grid(row=2, column=2)




f_top.pack(side=TOP, fill=BOTH, padx=[10, 10],pady=[10, 10])                 



             
#добавление раздела для настройки элементов графика (цвет, формат)
       

f_bot = LabelFrame(text="Настройка элементов графика")

l6 = Label(f_bot, text="Линии", borderwidth=5)
k1 = Button (f_bot, text="Настроить", borderwidth=2)

l10 = Label (f_bot, text="Фон", borderwidth=5)
k2 = Button (f_bot, text="Настроить", borderwidth=2)

l111 = Label (f_bot, text="Ось X", borderwidth=5)
k33 = Button (f_bot, text="Настроить", borderwidth=2)


spinbox_var = StringVar(value=1)
l11 = Label (f_bot, text="Ось Y", borderwidth=5)
k3 = Button (f_bot, text="Настроить", borderwidth=2)

spinbox_var1 = StringVar(value=1)
l12 = Label (f_bot, text="Заголовок", borderwidth=5)
k4 = Button (f_bot, text="Настроить", borderwidth=2)

spinbox_var2 = StringVar(value=1)
l13 = Label (f_bot, text="Сетка", borderwidth=5)
k5 = Button (f_bot, text="Настроить", borderwidth=2)




l15 = Label (f_bot, text="Легенда ", borderwidth=5)
k9 = Button (f_bot, text="Настроить", borderwidth=2)







l6.grid(row=0, column=0, padx=5, pady=5)
k1.grid(row=0, column=1, padx=5, pady=5)


l10.grid(row=1, column=0, padx=5, pady=5)
k2.grid(row=1, column=1, padx=5, pady=5)


l111.grid(row=2, column=0, padx=5, pady=5)
k33.grid(row=2, column=1, padx=5, pady=5)


l11.grid(row=3, column=0, padx=5, pady=5)
k3.grid(row=3, column=1, padx=5, pady=5)



l12.grid(row=4, column=0, padx=5, pady=5)
k4.grid(row=4, column=1, padx=5, pady=5)

l13.grid(row=5, column=0, padx=5, pady=5)
k5.grid(row=5, column=1, padx=5, pady=5)



l15.grid(row=7, column=0, padx=5, pady=5)

k9.grid(row=7, column=1, padx=5, pady=5)

f_bot.pack(side=RIGHT, fill=Y, padx=[10, 10], pady=[10, 10])  



f_down = LabelFrame()
l7 = Button(f_down, text="Очистить", borderwidth=5)
l8 = Button (f_down, text="Сохранить изображение", borderwidth=5)
l9 = Button (f_down, text="Сохранить в файл", borderwidth=5)
#l99 = Entry (f_down, width=67)



l7.grid(row=0, column=0, padx=5, pady=5)
l8.grid(row=0, column=1, padx=5, pady=5)
l9.grid(row=0, column=2, padx=5, pady=5)
#l99.grid(row=0, column=2, padx=5, pady=5)
f_down.pack(side=BOTTOM, padx=[10, 10], pady=[10, 10])     


#my_label = Label(root, text="Добавление функции", font=('Consolas', 20)).pack(side=RIGHT)

#my_button = Button (root, text="Generate Graph", borderwidth=5, command=Gen_graph) .pack()

canvas = Canvas (root)
canvas.pack(pady=18)
root.mainloop()