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
                 func="",
                 file="",
                 x_column=0,
                 y_column=1,
                 grid_color="grey",
                 grid_type=' ',
                 grid_thickness=0.5,
                 grid_axis='both',
                 legend='',
                 legend_location='best',
                 legend_fontsize=12,
                 legend_shadow=False,
                 marker_color="black",
                 marker_type="",
                 marker_size=1,
                 ):
        self.X = X
        self.Y = Y
        self.color = color
        self.line_type = line_type
        self.line_thick = line_thick
        self.x_label_text = x_label_text
        self.x_label_fontsize = x_label_fontsize
        self.x_label_color = x_label_color
        self.func = func
        self.file = file
        self.x_column = x_column
        self.y_column = y_column
        self.grid_color = grid_color
        self.grid_type = grid_type
        self.grid_thickness = grid_thickness
        self.grid_axis = grid_axis
        self.legend = legend
        self.legend_location = legend_location
        self.legend_fontsize = legend_fontsize
        self.legend_shadow = legend_shadow
        self.marker_color = marker_color
        self.marker_type = marker_type
        self.marker_size = marker_size

    def print_properties(self):
        print("X: ", self.X)
        print("Y: ", self.Y)
        print("color: ", self.color)
        print("line_type: ", self.line_type)
        print("line_thick: ", self.line_thick)
        print("x_label_text: ", self.x_label_text)
        print("x_label_fontsize: ", self.x_label_fontsize)
        print("x_label_color: ", self.x_label_color)
        print("func: ", self.func)
        print("file: ", self.file)
        print("x_column: ", self.x_column)
        print("y_column: ", self.y_column)
        print("grid_color: ", self.grid_color)
        print("grid_type: ", self.grid_type)
        print("grid_thickness: ", self.grid_thickness)
        print("grid_axis: ", self.grid_axis)
        print("legend: ", self.legend)
        print("legend_location : ", self.legend_location)
        print("legend_fontsize : ", self.legend_fontsize)
        print("legend_shadow : ", self.legend_shadow)
        print("marker_color : ", self.marker_color)
        print("marker_type : ", self.marker_type)
        print("marker_size : ", self.marker_size)
