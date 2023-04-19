from tkinter import *
from numpy import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import warnings


root = Tk()
root.geometry("995x773")
root.title("VApp")
warnings.filterwarnings("error")
func = {

}

# добавление канвы для построения графиков
def Gen_graph(event):
    try:
        mystr = function_field.get()
        exec('f = lambda x:' + mystr, globals())
        a = float(strA.get())
        b = float(strB.get())
        X = linspace(a, b, 300)
        Y = [f(x) for x in X]
        ax.clear()  # очистить графическую область
        ax.plot(X, Y, linewidth=2)
        canvasAgg.draw()  # перерисовать «составной» холст
        return
    except:  # реакция на любую ошибку
        showerror('Ошибка', "Неверное выражение или интервал [a,b].")

def Gen_graph2(event):  # чтобы кнопка отжималась при ошибке
    root.after(100, Gen_graph, event)




# окно ввода функции (объявление, построение)

f_top = LabelFrame(text="Добавление данных")
f_top.grid_columnconfigure(0, weight=1)
f_top.grid_columnconfigure(1, weight=2)
f_top.grid_columnconfigure(2, weight=1)
f_top.grid_columnconfigure(3, weight=1)

function_label = Label(f_top, width=30, height=2, text="Введите функцию:", anchor='w')
function_label.grid(row=0, column=0, columnspan=1)

function_field = Entry(f_top, width=30)
function_field.bind("<Return>", Gen_graph)
function_field.grid(row=0, column=1, columnspan=1)

interval_start_label = Label(f_top, width=30, height=2, text="Начало интервала a:", anchor='w')
interval_start_label.grid(row=1, column=0)

strA = StringVar()
strA.set(0)
interval_start_field = Entry(f_top, width=5, textvariable=strA)
interval_start_field.bind("<Return>", Gen_graph)
interval_start_field.grid(row=1, column=1)

interval_end_label = Label(f_top, width=15, height=2, text="Конец интервала b:")
interval_end_label.grid(row=1, column=2)

strB = StringVar()
strB.set(10)
interval_end_field = Entry(f_top, width=3, textvariable=strB)
interval_start_field.bind("<Return>", Gen_graph)
interval_end_field.grid(row=1, column=3)

build_button = Button(f_top, text="Построить", borderwidth=5)
build_button.bind("<Button-1>", Gen_graph2)
build_button.grid(row=0, column=5, ipadx=77, ipady=6, rowspan=3)


import_label = Label(f_top, width=30, height=2, text="Импортировать данные из файла", anchor='w')
import_label.grid(row=2, column=0, columnspan=1)

fileAdd_button = Button(f_top, text="Добавить файл", borderwidth=5)
fileAdd_button.grid(row=2, column=1)
#

f_top.pack(side=TOP, fill=BOTH, padx=[10, 10], pady=[10, 10])

# добавление раздела для настройки элементов графика (цвет, формат)

fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
ax = fig.add_subplot(111)
canvasAgg = FigureCanvasTkAgg(fig, master=root)
canvasAgg.draw()
canvas = canvasAgg.get_tk_widget()
canvas.pack(fill=BOTH, expand=1)

f_bot = LabelFrame(text="Настройка элементов графика")

l6 = Label(f_bot, text="Линии", borderwidth=5)
k1 = Button(f_bot, text="Настроить", borderwidth=2)

l10 = Label(f_bot, text="Фон", borderwidth=5)
k2 = Button(f_bot, text="Настроить", borderwidth=2)

l111 = Label(f_bot, text="Ось X", borderwidth=5)
k33 = Button(f_bot, text="Настроить", borderwidth=2)

spinbox_var = StringVar(value=1)
l11 = Label(f_bot, text="Ось Y", borderwidth=5)
k3 = Button(f_bot, text="Настроить", borderwidth=2)

spinbox_var1 = StringVar(value=1)
l12 = Label(f_bot, text="Заголовок", borderwidth=5)
k4 = Button(f_bot, text="Настроить", borderwidth=2)

spinbox_var2 = StringVar(value=1)
l13 = Label(f_bot, text="Сетка", borderwidth=5)
k5 = Button(f_bot, text="Настроить", borderwidth=2)

l15 = Label(f_bot, text="Легенда ", borderwidth=5)
k9 = Button(f_bot, text="Настроить", borderwidth=2)

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
l8 = Button(f_down, text="Сохранить изображение", borderwidth=5)
l9 = Button(f_down, text="Сохранить в файл", borderwidth=5)
l99 = Entry (f_down, width=67)


l7.grid(row=0, column=0, padx=5, pady=5)
l8.grid(row=0, column=1, padx=5, pady=5)
l9.grid(row=0, column=2, padx=5, pady=5)
# l99.grid(row=0, column=2, padx=5, pady=5)
f_down.pack(side=BOTTOM, padx=[10, 10], pady=[10, 10])



canvas = Canvas(root)
canvas.pack(pady=18)
root.bind('<Control-z>', lambda event: root.destroy())
root.mainloop()
