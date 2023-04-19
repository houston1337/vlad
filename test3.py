import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a label widget
        self.label = tk.Label(self, text="")
        self.label.pack()

        # Create a button that opens the second window
        self.button = tk.Button(self, text="Open Second Window", command=self.open_second_window)
        self.button.pack()

    def open_second_window(self):
        # Define the callback function
        def callback(data):
            self.label.configure(text="Hello, " + data + "!")

        # Create an instance of the SecondWindow class and pass the callback function
        SecondWindow(self, callback)


class SecondWindow(tk.Toplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback

        # Create a label and an entry widget
        label = tk.Label(self, text="Enter your name:")
        label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()

        # Create a button that calls the callback function
        button = tk.Button(self, text="OK", command=self.send_data)
        button.pack()

    def send_data(self):
        # Get the value of the entry widget
        data = self.entry.get()

        # Call the callback function and pass the data
        self.callback(data)


# Create an instance of the MainWindow class
main_window = MainWindow()

# Start the main event loop
main_window.mainloop()