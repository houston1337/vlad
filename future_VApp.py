
from tkinter import *
from numpy import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import warnings


def evaluate(event):
    try:
        mystr = entry.get()
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


def evaluate2(event):  # чтобы кнопка отжималась при ошибке
    root.after(100, evaluate, event)


root = Tk()
root.wm_title("График функции")
warnings.filterwarnings("error")
frameUp = Frame(root, relief=SUNKEN, height=64)
frameUp.pack(side=TOP, fill=X)
Label(frameUp, text="Выражение: ").place(x=20, y=4, width=100, height=25)
Label(frameUp, text="Начало интервала a:").place(x=250, y=4, width=140, height=25)
Label(frameUp, text="Конец интервала b:").place(x=370, y=4, width=140, height=25)
entry = Entry(frameUp, relief=RIDGE, borderwidth=4)
entry.bind("<Return>", evaluate)
entry.place(x=6, y=30, width=250, height=25)
strA = StringVar()
strA.set(0)
entryA = Entry(frameUp, relief=RIDGE, borderwidth=4, textvariable=strA)
entryA.place(x=280, y=30, width=80, height=25)
entryA.bind("<Return>", evaluate)
strB = StringVar()
strB.set(1)
entryB = Entry(frameUp, relief=RIDGE, borderwidth=4, textvariable=strB)
entryB.place(x=400, y=30, width=80, height=25)
entryB.bind("<Return>", evaluate)
fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
ax = fig.add_subplot(111)
canvasAgg = FigureCanvasTkAgg(fig, master=root)
canvasAgg.draw()
canvas = canvasAgg.get_tk_widget()
canvas.pack(fill=BOTH, expand=1)
btn = Button(root, text='График')
btn.bind("<Button-1>", evaluate2)
btn.pack(ipady=2, pady=4, padx=10)
root.bind('<Control-z>', lambda event: root.destroy())
root.mainloop()
