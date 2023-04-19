from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x225")
root.title ("Настройка легенды")



line_settings = LabelFrame(text="Настройка легенды")


l1 = Label(line_settings, width=15, height=2,text="Текст:")
l4 = Entry (line_settings, width=21)

line_color = Label(line_settings, text="Положение легенды", borderwidth=5)
line_color_combo = ttk.Combobox(line_settings, values=[ "Верхний правый",  "Верхний левый",   "Нижний левый",   "Нижний правый",   "Центр слева",   "Центр",   "Центр справа",   "Нижний центр",   "Верхний центр"])


type_line = Label (line_settings, text="Тень легенды", borderwidth=5) 
type_line_combo = ttk.Combobox(line_settings, values=[ "Добавить",  "Убрать"])

spinbox_var = StringVar(value=1)
thick_line = Label (line_settings, text="Размер шрифта", borderwidth=5)
thick_line_spin = Spinbox(line_settings, from_= 0, to = 10,width=5, textvariable=spinbox_var)



l1.grid(row=0, column=0, padx=5, pady=5)
l4.grid(row=0, column=1, padx=5, pady=5)

line_color.grid(row=1, column=0, padx=5, pady=5)
line_color_combo.grid(row=1, column=1, padx=5, pady=5)
line_color_combo.current(0)

type_line.grid(row=2, column=0, padx=5, pady=5)
type_line_combo.grid(row=2, column=1, padx=5, pady=5)
type_line_combo.current(0)

thick_line.grid(row=3, column=0, padx=5, pady=5)
thick_line_spin.grid(row=3, column=1, padx=5, pady=5)


line_settings.pack(fill=Y)  



ok = Button (root, text="Применить", borderwidth=2)
ok.pack(side=TOP,fill=X)


root.mainloop()