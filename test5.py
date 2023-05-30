from tkinter import *
from tkinter import ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import customtkinter as ctk
from info import Info
from Line import Lines
from OX import Ox
from OY import Oy
from SingleFile import SingleFile
from graphSettings import GraphSettings
from MultipleFiles import multipleFile
from math import *
from Grid import Grid
from Legend import Legend
import os
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from tkinter import filedialog
from Title import Title
from Background import Background


class App(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("995x773")
        self.title("VApp")
        ctk.set_appearance_mode("dark")

        self.fTop = LabelFrame(text="Добавление данных")
        self.fTop.grid_columnconfigure(0, weight=1)
        self.fTop.grid_columnconfigure(1, weight=1)
        self.fTop.grid_columnconfigure(2, weight=1)
        self.fTop.grid_columnconfigure(4, weight=1)
        self.function_label = ttk.Label(self.fTop, text="Введите функцию:", justify=LEFT)
        self.function_label.grid(row=0, column=0, sticky=W, padx=12)

        self.strFunc = StringVar()
        # self.strFunc.set("x")
        self.strFunc.set("")
        self.functionField = ttk.Entry(self.fTop, width=20, textvariable=self.strFunc, justify=LEFT)
        self.functionField.bind("<Return>", self.gen_graph2)
        self.functionField.grid(row=0, column=1, sticky=W)

        self.addNew = ttk.Button(self.fTop, text="Добавить новый", width=20, command=self.createNewGraph)
        self.addNew.grid(row=0, column=2, sticky=W)
        #
        # self.goToLabel = ttk.Label(self.fTop, text="Перейти к:", justify=LEFT)
        # self.goToLabel.grid(row=0, column=3, sticky=W)
        # self.goTo = StringVar()
        # self.goTo.set(0)
        # self.goToField = ttk.Entry(self.fTop, width=5, textvariable=self.goTo, justify=LEFT)
        # self.goToField.grid(row=0, column=4)
        # self.goToButton = ttk.Button(self.fTop, text="ok", command=self.set_curret)
        # self.goToButton.grid(row=0, column=5, sticky=W)

        self.goToLabel = ttk.Label(self.fTop, text="Перейти к:", justify=LEFT)
        self.goToLabel.grid(row=0, column=3, sticky=W)
        self.goTo = StringVar()
        self.goTo.set(1)
        self.goToField = Spinbox(self.fTop, width=5, from_=1, to=1, textvariable=self.goTo, justify=LEFT)
        self.goToField.grid(row=0, column=4)
        self.goToButton = ttk.Button(self.fTop, text="ok", command=self.set_curret)
        self.goToButton.grid(row=0, column=5, sticky=W)

        self.buildButton = ttk.Button(self.fTop, text="Построить", command=self.gen_graph)
        self.buildButton.grid(row=1, column=5, ipadx=77, ipady=6)

        self.intervalStartLabel = ttk.Label(self.fTop, text="Начало интервала a:", justify=LEFT)
        self.intervalStartLabel.grid(row=1, column=0, sticky=W, padx=12)
        self.strA = StringVar()
        self.strA.set(0)
        self.start = ttk.Entry(self.fTop, width=10, textvariable=self.strA)
        self.start.grid(row=1, column=1, sticky=W)

        self.intervalEndLabel = Label(self.fTop, width=15, height=2, text="Конец интервала b:", justify=LEFT)
        self.intervalEndLabel.grid(row=1, column=2, sticky=W)
        self.strB = StringVar()
        self.strB.set(10)
        self.end = ttk.Entry(self.fTop, width=10, textvariable=self.strB)
        self.end.grid(row=1, column=3, sticky=W)

        self.importLabel = Label(self.fTop, text="Файл с \nтабличными значениями", justify=LEFT)
        self.importLabel.grid(row=2, column=0, sticky=W, padx=12)
        self.importBtn = ttk.Button(self.fTop, text="Добавить файл", width=20, command=self.read_from_file)
        self.importBtn.grid(row=2, column=1, sticky=W)

        self.strFile = StringVar()
        # self.strFile.set("C:/Users/Egor/Desktop/vlad/data/ampl1.csv")
        self.strFile.set("")
        self.fileField = ttk.Entry(self.fTop, width=51, textvariable=self.strFile, state=DISABLED)
        self.fileField.bind("<Return>", self.gen_graph2)
        self.fileField.grid(row=2, column=2, sticky=W, columnspan=4)

        self.isUseFile = BooleanVar()
        self.useDataFromFile = ttk.Checkbutton(self.fTop, text="Использовать данные из файла", variable=self.isUseFile)
        self.useDataFromFile.grid(row=2, column=5, sticky=W)

        self.batchLabel = Label(self.fTop, text="Пакетная обработка", justify=LEFT)
        self.batchLabel.grid(row=3, column=0, sticky=W, padx=12, pady=10)
        self.batchBtn = ttk.Button(self.fTop, text="Добавить файлы", width=20, command=self.open_multi)
        self.batchBtn.grid(row=3, column=1, sticky=W)

        self.strFiles = StringVar()
        # self.strFiles.set("ampl1.csv, ampl2.csv ...")
        self.strFiles.set("")
        self.filesField = ttk.Entry(self.fTop, width=20, textvariable=self.strFiles)
        self.filesField.grid(row=3, column=2, sticky=W)

        self.isDrawAll = BooleanVar()
        self.DrawAll = ttk.Checkbutton(self.fTop, text="Построить все", variable=self.isDrawAll)
        self.DrawAll.grid(row=3, column=5, sticky=W)

        self.fTop.pack(side=TOP, fill=X, padx=10, pady=10)

        # добавление раздела для настройки элементов графика (цвет, формат)

        self.fBottom = LabelFrame(text="Настройка элементов графика")

        self.linesLabel = Label(self.fBottom, text="Линии", borderwidth=5)
        self.linesLabel.grid(row=0, column=0, padx=5, pady=5)
        self.linesBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_lines)
        self.linesBtn.grid(row=0, column=1, padx=5, pady=5)

        self.backgroundLabel = Label(self.fBottom, text="Фон", borderwidth=5)
        self.backgroundLabel.grid(row=1, column=0, padx=5, pady=5)
        self.backgroundBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_background)
        self.backgroundBtn.grid(row=1, column=1, padx=5, pady=5)

        self.xAxisLabel = Label(self.fBottom, text="Ось X", borderwidth=5)
        self.xAxisLabel.grid(row=2, column=0, padx=5, pady=5)
        self.xAxisBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_OX)
        self.xAxisBtn.grid(row=2, column=1, padx=5, pady=5)

        self.yAxisLabel = Label(self.fBottom, text="Ось Y", borderwidth=5)
        self.yAxisLabel.grid(row=3, column=0, padx=5, pady=5)
        self.yAxisBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_OY)
        self.yAxisBtn.grid(row=3, column=1, padx=5, pady=5)

        self.headerLabel = Label(self.fBottom, text="Заголовок", borderwidth=5)
        self.headerLabel.grid(row=4, column=0, padx=5, pady=5)
        self.headerBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_title)
        self.headerBtn.grid(row=4, column=1, padx=5, pady=5)

        self.gridLabel = Label(self.fBottom, text="Сетка", borderwidth=5)
        self.gridLabel.grid(row=5, column=0, padx=5, pady=5)
        self.gridBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_grid)
        self.gridBtn.grid(row=5, column=1, padx=5, pady=5)

        self.legendLabel = Label(self.fBottom, text="Легенда ", borderwidth=5)
        self.legendLabel.grid(row=7, column=0, padx=5, pady=5)
        self.legendBtn = ttk.Button(self.fBottom, text="Настроить", command=self.open_legend)
        self.legendBtn.grid(row=7, column=1, padx=5, pady=5)

        self.setAllLabel = Label(self.fBottom, text="Применить стандартную \nнастройку для всех", borderwidth=5)
        self.setAllLabel.grid(row=8, column=0, padx=5, pady=5)
        self.setAllBtn = ttk.Button(self.fBottom, text="ок", command=self.set_all)
        self.setAllBtn.grid(row=8, column=1, padx=5, pady=5)

        self.fBottom.pack(side=RIGHT, fill=Y, padx=10, pady=10)

        self.fDown = LabelFrame()

        self.clearBtn = ttk.Button(self.fDown, text="Очистить", command=self.clear)
        self.clearBtn.grid(row=0, column=0, padx=5, pady=5)

        self.saveBtn = ttk.Button(self.fDown, text="Сохранить все", command=self.save_all)
        self.saveBtn.grid(row=0, column=1, padx=5, pady=5)

        self.saveBtn = ttk.Button(self.fDown, text="Сохранить как", command=self.open_save)
        self.saveBtn.grid(row=0, column=2, padx=5, pady=5)

        self.saveBtn = ttk.Button(self.fDown, text="Справка", command=self.open_info)
        self.saveBtn.grid(row=0, column=3, padx=5, pady=5)

        # self.l9 = Button(self.fDown, text="Сохранить в файл", borderwidth=5)
        # self.l9.grid(row=0, column=2, padx=5, pady=5)
        self.fDown.pack(side=BOTTOM, padx=[10, 10], pady=[10, 10])

        self.fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
        self.ax = self.fig.add_subplot(111)
        self.canvasAgg = FigureCanvasTkAgg(self.fig, master=self)
        self.canvasAgg.draw()
        self.canvas = self.canvasAgg.get_tk_widget()
        self.canvas.pack(fill=BOTH, expand=1)

    currentGraphIndex = 0
    lastAddedIndex = 1
    graphs = np.array([GraphSettings(X=[], Y=[])])

    default_color = "black"
    default_line_type = "-"
    default_line_thick = 1
    default_x_label_text = " "
    default_x_label_fontsize = 12
    default_x_label_color = "black"
    default_x_major_locator = 1
    default_x_minor_locator = 1

    default_y_label_text = " "
    default_y_label_fontsize = 12
    default_y_label_color = "black"
    default_y_major_locator = 1
    default_y_minor_locator = 1

    default_grid_color = "grey"
    default_grid_type = ' '
    default_grid_thickness = 0.5
    default_grid_axis = 'both'
    default_is_show_legend = False
    default_legend = ''
    default_legend_location = 'best'
    default_legend_fontsize = 12
    default_legend_shadow = False
    default_marker_color = "black"
    default_marker_type = ""
    default_marker_size = 1

    default_title_text = ''
    default_title_fontsize = 12
    default_title_text_color = 'black'
    default_title_text_position = 'center'
    default_title_background_color = 'white'
    default_background_color = 'white'
    default_background_color_alpha = 1.0
    default_save_path = ''

    def open_info(self):
        Info(self)

    def open_grid(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].grid_color, \
            self.graphs[self.currentGraphIndex].grid_type, \
            self.graphs[self.currentGraphIndex].grid_thickness, \
            self.graphs[self.currentGraphIndex].grid_axis = data

        Grid(self, callback,
             self.graphs[self.currentGraphIndex].grid_color,
             self.graphs[self.currentGraphIndex].grid_type,
             self.graphs[self.currentGraphIndex].grid_thickness,
             self.graphs[self.currentGraphIndex].grid_axis)

    def open_legend(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].legend, \
            self.graphs[self.currentGraphIndex].legend_location, \
            self.graphs[self.currentGraphIndex].legend_fontsize, \
            self.graphs[self.currentGraphIndex].legend_shadow, \
            self.graphs[self.currentGraphIndex].is_show_legend = data

        Legend(self, callback,
               self.graphs[self.currentGraphIndex].legend,
               self.graphs[self.currentGraphIndex].legend_location,
               self.graphs[self.currentGraphIndex].legend_fontsize,
               self.graphs[self.currentGraphIndex].legend_shadow,
               self.graphs[self.currentGraphIndex].is_show_legend,
               )

    def open_background(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].background_color, \
            self.graphs[self.currentGraphIndex].background_color_alpha = data

        Background(self, callback,
                   self.graphs[self.currentGraphIndex].background_color,
                   self.graphs[self.currentGraphIndex].background_color_alpha)

    def open_title(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].title_text, \
            self.graphs[self.currentGraphIndex].title_fontsize, \
            self.graphs[self.currentGraphIndex].title_text_color, \
            self.graphs[self.currentGraphIndex].title_text_position, \
            self.graphs[self.currentGraphIndex].title_background_color = data

        Title(self, callback,
              self.graphs[self.currentGraphIndex].title_text,
              self.graphs[self.currentGraphIndex].title_fontsize,
              self.graphs[self.currentGraphIndex].title_text_color,
              self.graphs[self.currentGraphIndex].title_text_position,
              self.graphs[self.currentGraphIndex].title_background_color
              )

    def open_lines(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].color, \
            self.graphs[self.currentGraphIndex].line_type, \
            self.graphs[self.currentGraphIndex].line_thick, \
            self.graphs[self.currentGraphIndex].marker_color, \
            self.graphs[self.currentGraphIndex].marker_type, \
            self.graphs[self.currentGraphIndex].marker_size = data

        Lines(self, callback,
              self.graphs[self.currentGraphIndex].color,
              self.graphs[self.currentGraphIndex].line_type,
              self.graphs[self.currentGraphIndex].line_thick,
              self.graphs[self.currentGraphIndex].marker_color,
              self.graphs[self.currentGraphIndex].marker_type,
              self.graphs[self.currentGraphIndex].marker_size
              )

    def open_OX(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].x_label_text, \
            self.graphs[self.currentGraphIndex].x_label_fontsize, \
            self.graphs[self.currentGraphIndex].x_label_color, \
            self.graphs[self.currentGraphIndex].x_major_locator, \
            self.graphs[self.currentGraphIndex].x_minor_locator \
                = data

        Ox(self, callback,
           self.graphs[self.currentGraphIndex].x_label_text,
           self.graphs[self.currentGraphIndex].x_label_fontsize,
           self.graphs[self.currentGraphIndex].x_label_color,
           self.graphs[self.currentGraphIndex].x_major_locator,
           self.graphs[self.currentGraphIndex].x_minor_locator,
           )

    def open_OY(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].y_label_text, \
            self.graphs[self.currentGraphIndex].y_label_fontsize, \
            self.graphs[self.currentGraphIndex].y_label_color, \
            self.graphs[self.currentGraphIndex].y_major_locator, \
            self.graphs[self.currentGraphIndex].y_minor_locator \
                = data

        Oy(self, callback,
           self.graphs[self.currentGraphIndex].y_label_text,
           self.graphs[self.currentGraphIndex].y_label_fontsize,
           self.graphs[self.currentGraphIndex].y_label_color,
           self.graphs[self.currentGraphIndex].y_major_locator,
           self.graphs[self.currentGraphIndex].y_minor_locator,
           )

    def open_multi(self):
        multipleFile(self)

    def open_save(self):
        self.graphs[self.currentGraphIndex].save_path = filedialog.asksaveasfilename(
            initialdir="C:/Users/Egor/Desktop/vlad",
            title="Save file",
            filetypes=(("jpg files", "*.jpg"),
                       ("eps files", "*.eps"),
                       ("png files", "*.png"),
                       ("all files", "*.*")))
        self.default_save_path = self.graphs[self.currentGraphIndex].save_path
        print(self.graphs[self.currentGraphIndex].save_path)
        self.save()

    def read_from_file(self):
        def callback(data):
            self.graphs[self.currentGraphIndex].X, \
            self.graphs[self.currentGraphIndex].Y, \
            self.graphs[self.currentGraphIndex].file, \
            self.graphs[self.currentGraphIndex].x_column, \
            self.graphs[self.currentGraphIndex].y_column = data
            self.strFile.set(self.graphs[self.currentGraphIndex].file)

        SingleFile(self, callback, self.strFile.get(), x_column=self.graphs[self.currentGraphIndex].x_column,
                   y_column=self.graphs[self.currentGraphIndex].y_column)
        self.isUseFile.set(True)

    # TODO - передесать чтобы не открывалось лишнее окно
    # def read_from_file2(self):
    #     def callback(data):
    #         self.graphs[self.currentGraphIndex].X, \
    #         self.graphs[self.currentGraphIndex].Y, \
    #         self.graphs[self.currentGraphIndex].strFile, \
    #         self.graphs[self.currentGraphIndex].x_column, \
    #         self.graphs[self.currentGraphIndex].y_column, = data
    #         self.strFile.set(self.graphs[self.currentGraphIndex].strFile)
    #
    #     SingleFile(self, callback, self.strFile.get(), x_column=self.graphs[self.currentGraphIndex].x_column,
    #                y_column=self.graphs[self.currentGraphIndex].y_column).send_data()

    def save_all(self):
        self.open_save()
        for graph in range(len(self.graphs)):
            self.set_curret(graph)
            self.gen_graph()
            self.canvasAgg.print_figure(self.default_save_path + str(graph) + ".jpg")

    def save(self):
        self.gen_graph()
        self.canvasAgg.print_figure(self.graphs[self.currentGraphIndex].save_path)

    def clear(self):
        self.ax.clear()
        self.canvasAgg.draw()

        # def defineX(self):
        #     if (not (self.isUseFile.get())):
        #         self.graphs[self.currentGraphIndex].X = np.linspace(a, b, 5)

    def gen_graph(self):
        # try:

        a = float(self.start.get())
        b = float(self.end.get())
        # print(str(a) + " " + str(b))
        # если используется строка ввода функции
        if (not (self.isUseFile.get())):
            self.graphs[self.currentGraphIndex].func = self.functionField.get()
            exec('f = lambda x:' + self.graphs[self.currentGraphIndex].func, globals())
            self.graphs[self.currentGraphIndex].X = np.linspace(a, b, 500)
            self.graphs[self.currentGraphIndex].Y = [f(x) for x in self.graphs[self.currentGraphIndex].X]
            if self.graphs[self.currentGraphIndex].legend == '' and self.graphs[self.currentGraphIndex].is_show_legend:
                self.graphs[self.currentGraphIndex].legend = self.graphs[self.currentGraphIndex].func
        else:
            if self.graphs[self.currentGraphIndex].legend == '' and self.graphs[self.currentGraphIndex].is_show_legend:
                self.graphs[self.currentGraphIndex].legend = os.path.basename(self.graphs[self.currentGraphIndex].file)

        self.ax.clear()  # очистить графическую область
        # рисуем все графики на одном холсте
        if (self.isDrawAll.get()):
            for graph in self.graphs:
                self.ax.plot(
                    graph.X,
                    graph.Y,
                    color=graph.color,
                    linestyle=graph.line_type,
                    linewidth=graph.line_thick,
                    marker=graph.marker_type,
                    markersize=graph.marker_size,
                    markerfacecolor=graph.marker_color,
                    markeredgecolor=graph.marker_color,
                )
                if (self.graphs[self.currentGraphIndex].is_show_legend):
                    self.ax.plot(
                        graph.X,
                        graph.Y,
                        color=graph.color,
                        linestyle=graph.line_type,
                        linewidth=graph.line_thick,
                        label=graph.legend,
                        marker=graph.marker_type,
                        markersize=graph.marker_size,
                        markerfacecolor=graph.marker_color,
                        markeredgecolor=graph.marker_color,
                    )

                    self.ax.legend(loc=graph.legend_location,
                                    shadow=graph.legend_shadow,
                                    fontsize=graph.legend_fontsize)
        # для одного графика на полотне
        else:
            # если легенда включена
            if (self.graphs[self.currentGraphIndex].is_show_legend):
                self.ax.plot(
                    self.graphs[self.currentGraphIndex].X,
                    self.graphs[self.currentGraphIndex].Y,
                    color=self.graphs[self.currentGraphIndex].color,
                    linestyle=self.graphs[self.currentGraphIndex].line_type,
                    linewidth=self.graphs[self.currentGraphIndex].line_thick,
                    label=self.graphs[self.currentGraphIndex].legend,
                    marker=self.graphs[self.currentGraphIndex].marker_type,
                    markersize=self.graphs[self.currentGraphIndex].marker_size,
                    markerfacecolor=self.graphs[self.currentGraphIndex].marker_color,
                    markeredgecolor=self.graphs[self.currentGraphIndex].marker_color,
                )
                self.ax.legend(loc=self.graphs[self.currentGraphIndex].legend_location,
                               shadow=self.graphs[self.currentGraphIndex].legend_shadow,
                               fontsize=self.graphs[self.currentGraphIndex].legend_fontsize)
            # если легенда отключена
            else:
                self.ax.plot(
                    self.graphs[self.currentGraphIndex].X,
                    self.graphs[self.currentGraphIndex].Y,
                    color=self.graphs[self.currentGraphIndex].color,
                    linestyle=self.graphs[self.currentGraphIndex].line_type,
                    linewidth=self.graphs[self.currentGraphIndex].line_thick,
                    marker=self.graphs[self.currentGraphIndex].marker_type,
                    markersize=self.graphs[self.currentGraphIndex].marker_size,
                    markerfacecolor=self.graphs[self.currentGraphIndex].marker_color,
                    markeredgecolor=self.graphs[self.currentGraphIndex].marker_color,
                )

        # подпись по Х
        self.ax.xaxis.set_major_locator(MultipleLocator(self.graphs[self.currentGraphIndex].x_major_locator))
        self.ax.xaxis.set_major_formatter('{x:.0f}')
        self.ax.xaxis.set_minor_locator(MultipleLocator(self.graphs[self.currentGraphIndex].x_minor_locator))

        self.ax.set_xlabel(
            self.graphs[self.currentGraphIndex].x_label_text,
            fontsize=self.graphs[self.currentGraphIndex].x_label_fontsize,
            color=self.graphs[self.currentGraphIndex].x_label_color)

        # подпись по Y
        self.ax.yaxis.set_major_locator(MultipleLocator(self.graphs[self.currentGraphIndex].y_major_locator))
        self.ax.yaxis.set_major_formatter('{x:.0f}')
        self.ax.yaxis.set_minor_locator(MultipleLocator(self.graphs[self.currentGraphIndex].y_minor_locator))

        self.ax.set_ylabel(
            self.graphs[self.currentGraphIndex].y_label_text,
            fontsize=self.graphs[self.currentGraphIndex].y_label_fontsize,
            color=self.graphs[self.currentGraphIndex].y_label_color)

        # настройка сетки
        self.ax.grid(color=self.graphs[self.currentGraphIndex].grid_color,
                     linestyle=self.graphs[self.currentGraphIndex].grid_type,
                     linewidth=self.graphs[self.currentGraphIndex].grid_thickness,
                     axis=self.graphs[self.currentGraphIndex].grid_axis)

        # настройка заголовка
        self.ax.set_title(
            self.graphs[self.currentGraphIndex].title_text,
            loc=self.graphs[self.currentGraphIndex].title_text_position,
            fontsize=self.graphs[self.currentGraphIndex].title_fontsize,
            backgroundcolor=self.graphs[self.currentGraphIndex].title_background_color,
            color=self.graphs[self.currentGraphIndex].title_text_color,
        )

        # настройка фона
        self.ax.set_facecolor(self.graphs[self.currentGraphIndex].background_color)
        self.ax.patch.set_alpha(self.graphs[self.currentGraphIndex].background_color_alpha)

        # self.fig.set_facecolor('red')

        self.canvasAgg.draw()  # перерисовать «составной» холст
        self.print_current()
        return
        # except:  # реакция на любую ошибку
        #     showerror('Ошибка', "Неверное выражение или интервал [a,b].")

    def gen_graph2(self, event):  # чтобы кнопка отжималась при ошибке
        self.after(100, self.gen_graph)

    def print_current(self):
        self.graphs[self.currentGraphIndex].print_properties()

    def createNewGraph(self, x=[], y=[],
                       file="",
                       x_column=0,
                       y_column=1,
                       ):
        self.strFunc.set("")
        self.strFile.set(file)
        self.lastAddedIndex += 1
        self.currentGraphIndex = self.lastAddedIndex - 1
        self.graphs = np.append(self.graphs, [GraphSettings(X=x, Y=y, file=file,
                                                            x_column=x_column, y_column=y_column,
                                                            color=self.default_color,
                                                            line_type=self.default_line_type,
                                                            line_thick=self.default_line_thick,
                                                            x_label_text=self.default_x_label_text,
                                                            x_label_fontsize=self.default_x_label_fontsize,
                                                            x_label_color=self.default_x_label_color,
                                                            x_major_locator=self.default_x_major_locator,
                                                            x_minor_locator=self.default_x_minor_locator,

                                                            y_label_text=self.default_y_label_text,
                                                            y_label_fontsize=self.default_y_label_fontsize,
                                                            y_label_color=self.default_y_label_color,
                                                            y_major_locator=self.default_y_major_locator,
                                                            y_minor_locator=self.default_y_minor_locator,

                                                            grid_color=self.default_grid_color,
                                                            grid_type=self.default_grid_type,
                                                            grid_thickness=self.default_grid_thickness,
                                                            grid_axis=self.default_grid_axis,
                                                            is_show_legend=self.default_is_show_legend,
                                                            legend=self.default_legend,
                                                            legend_location=self.default_legend_location,
                                                            legend_fontsize=self.default_legend_fontsize,
                                                            legend_shadow=self.default_legend_shadow,
                                                            marker_color=self.default_marker_color,
                                                            marker_type=self.default_marker_type,
                                                            marker_size=self.default_marker_size,

                                                            title_text=self.default_title_text,
                                                            title_fontsize=self.default_title_fontsize,
                                                            title_text_color=self.default_title_text_color,
                                                            title_text_position=self.default_title_text_position,
                                                            title_background_color=self.default_title_background_color,

                                                            background_color=self.default_background_color,
                                                            background_color_alpha=self.default_background_color_alpha,
                                                            )])

        self.goToField = Spinbox(self.fTop, width=5, from_=1, to=self.graphs.shape[0], textvariable=self.goTo,
                                 justify=LEFT)
        self.goToField.grid(row=0, column=4)
        if (not (file == "")):
            self.isUseFile.set(True)
        # self.print_current()

    def set_all(self):
        for graph in self.graphs:
            graph.color = self.default_color
            graph.line_type = self.default_line_type
            graph.line_thick = self.default_line_thick
            graph.x_label_text = self.default_x_label_text
            graph.x_label_fontsize = self.default_x_label_fontsize
            graph.x_label_color = self.default_x_label_color
            graph.x_major_locator = self.default_x_major_locator
            graph.x_minor_locator = self.default_x_minor_locator

            graph.y_label_text = self.default_y_label_text
            graph.y_label_fontsize = self.default_y_label_fontsize
            graph.y_label_color = self.default_y_label_color
            graph.y_major_locator = self.default_y_major_locator
            graph.y_minor_locator = self.default_y_minor_locator

            graph.grid_color = self.default_grid_color
            graph.grid_type = self.default_grid_type
            graph.grid_thickness = self.default_grid_thickness
            graph.grid_axis = self.default_grid_axis
            graph.is_show_legend = self.default_is_show_legend
            graph.legend = self.default_legend
            graph.legend_location = self.default_legend_location
            graph.legend_fontsize = self.default_legend_fontsize
            graph.legend_shadow = self.default_legend_shadow
            graph.marker_color = self.default_marker_color
            graph.marker_type = self.default_marker_type
            graph.marker_size = self.default_marker_size

            graph.title_text = self.default_title_text
            graph.title_fontsize = self.default_title_fontsize
            graph.title_text_color = self.default_title_text_color
            graph.title_text_position = self.default_title_text_position
            graph.title_background_color = self.default_title_background_color

            graph.background_color = self.default_background_color
            graph.background_color_alpha = self.default_background_color_alpha

    def set_curret(self, *args):

        if (len(args) <= 0):
            if (self.goTo.get() < str(0) or self.goTo.get() > str(self.lastAddedIndex)):
                showerror('Ошибка', "Графика не найдено")
            else:
                self.currentGraphIndex = int(self.goTo.get()) - 1
                self.strFunc.set(self.graphs[self.currentGraphIndex].func)
                self.strFile.set(self.graphs[self.currentGraphIndex].file)
        else:
            self.currentGraphIndex = int(args[0])
            self.strFunc.set(self.graphs[self.currentGraphIndex].func)
            self.strFile.set(self.graphs[self.currentGraphIndex].file)

    def printAll(self):
        for graph in self.graphs:
            print("func ", graph.func)
            print("X ", graph.X)
            print("Y ", graph.Y)
            print("color ", graph.color)
            print("line_type ", graph.line_type)
            print("line_thick ", graph.line_thick)
            print("\n_______________________________________________\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
