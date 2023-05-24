import os


class GraphSettings:
    def __init__(self,
                 X, Y,
                 color="black",
                 line_type="-",
                 line_thick=1,
                 x_label_text=" ",
                 x_label_fontsize=12,
                 x_label_color="black",
                 x_major_locator=1,
                 x_minor_locator=1,

                 y_label_text=" ",
                 y_label_fontsize=12,
                 y_label_color="black",
                 y_major_locator=1,
                 y_minor_locator=1,

                 func="",
                 file="",
                 x_column=0,
                 y_column=1,
                 grid_color="grey",
                 grid_type=' ',
                 grid_thickness=0.5,
                 grid_axis='both',
                 is_show_legend=False,
                 legend='',
                 legend_location='best',
                 legend_fontsize=12,
                 legend_shadow=False,
                 marker_color="black",
                 marker_type="",
                 marker_size=1,

                 title_text='',
                 title_fontsize='12',
                 title_text_color='black',
                 title_text_position='center',
                 title_background_color='white',

                 background_color='white',
                 background_color_alpha=1.0,
                 save_path='1.jpg'):
        self.X = X
        self.Y = Y

        # Линия file - Line
        self.color = color
        self.line_type = line_type
        self.line_thick = line_thick

        self.marker_color = marker_color
        self.marker_type = marker_type
        self.marker_size = marker_size

        #  Подписи оси Х file - OX
        self.x_label_text = x_label_text
        self.x_label_fontsize = x_label_fontsize
        self.x_label_color = x_label_color
        self.x_major_locator = x_major_locator
        self.x_minor_locator = x_minor_locator

        #  Подписи оси Y file - OY
        self.y_label_text = y_label_text
        self.y_label_fontsize = y_label_fontsize
        self.y_label_color = y_label_color
        self.y_major_locator = y_major_locator
        self.y_minor_locator = y_minor_locator

        #  Функция file - main
        self.func = func

        # Путь к файлу file - SingleFile, MultipleFiles
        self.file = file
        self.x_column = x_column
        self.y_column = y_column

        # Настройка сетки file - Grid
        self.grid_color = grid_color
        self.grid_type = grid_type
        self.grid_thickness = grid_thickness
        self.grid_axis = grid_axis

        # Настройка легенды file - Legend
        self.legend = legend
        self.legend_location = legend_location
        self.legend_fontsize = legend_fontsize
        self.legend_shadow = legend_shadow
        self.is_show_legend = is_show_legend

        # Настройка заголовка file - Title
        self.title_text = title_text
        self.title_fontsize = title_fontsize
        self.title_text_color = title_text_color
        self.title_text_position = title_text_position
        self.title_background_color = title_background_color

        # Фон
        self.background_color = background_color
        self.background_color_alpha = background_color_alpha

        # Путь сохранения - file - Main
        self.save_path = save_path

    def print_properties(self):
        print("X: ", self.X)
        print("Y: ", self.Y)

        print("color: ", self.color)
        print("line_type: ", self.line_type)
        print("line_thick: ", self.line_thick)

        print("x_label_text: ", self.x_label_text)
        print("x_label_fontsize: ", self.x_label_fontsize)
        print("x_label_color: ", self.x_label_color)
        print("x_major_locator: ", self.x_major_locator)
        print("x_minor_locator: ", self.x_minor_locator)

        print("y_label_text: ", self.y_label_text)
        print("y_label_fontsize: ", self.y_label_fontsize)
        print("y_label_color: ", self.y_label_color)
        print("y_major_locator: ", self.y_major_locator)
        print("y_minor_locator: ", self.y_minor_locator)

        print("func: ", self.func)
        print("file: ", self.file)
        print("x_column: ", self.x_column)
        print("y_column: ", self.y_column)
        print("grid_color: ", self.grid_color)
        print("grid_type: ", self.grid_type)
        print("grid_thickness: ", self.grid_thickness)
        print("grid_axis: ", self.grid_axis)
        print("legend: ", self.legend)
        print("is_show_legend: ", self.is_show_legend)
        print("legend_location : ", self.legend_location)
        print("legend_fontsize : ", self.legend_fontsize)
        print("legend_shadow : ", self.legend_shadow)
        print("marker_color : ", self.marker_color)
        print("marker_type : ", self.marker_type)
        print("marker_size : ", self.marker_size)

        print("title_text : ", self.title_text)
        print("title_fontsize : ", self.title_fontsize)
        print("title_text_color : ", self.title_text_color)
        print("title_text_position : ", self.title_text_position)
        print("title_background_color : ", self.title_background_color)

        print("background_color : ", self.background_color)
        print("background_color_alpha : ", self.background_color_alpha)
