import tkinter as tk


class Window(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        button = tk.Button(self, text="Open window", command=self.onClick)
        button.pack(padx=50, pady=50)

    def onClick(self):
        var, note = Settings()
        print(f"Entry Widget: {note.get()}  RadioButton: {var.get()}")


def Settings():
    settingsWindow = tk.Toplevel()
    tk.Label(settingsWindow, text="Settings Window").grid(row=0)

    var = tk.IntVar()
    tk.Radiobutton(settingsWindow, text="Option1", variable=var,
                   value=1).grid(row=2, sticky="w", padx=5, pady=5)
    tk.Radiobutton(settingsWindow, text="Option2", variable=var,
                   value=2).grid(row=3, sticky="w", padx=5, pady=5)

    evar = tk.StringVar()
    note = tk.Entry(settingsWindow, width=30,
                    textvariable=evar).grid(row=6, padx=5, pady=5)

    Button = tk.Button(settingsWindow, text="Submit Data",
                       command=settingsWindow.destroy).grid(row=7)

    settingsWindow.wait_window()
    print("finished waiting...")
    return (var, evar)


root = tk.Tk()
Window(root).pack(side="top", fill="both", expand=True)
root.mainloop()