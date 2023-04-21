class GraphSettings:
    def __init__(self,
                 X, Y,
                 color="black",
                 line_type="-",
                 line_thick=1,
                 x_label_text=" ",
                 x_label_fontsize=12,
                 x_label_color="black",
                 func=""
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