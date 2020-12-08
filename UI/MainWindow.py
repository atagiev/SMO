import tkinter as tk
from UI.StepModeWindow import StepModeWindow
from UI.AutomaticModeWindow import AutomaticModeWindow
from UI.ConfigWindow import ConfigWindow

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SMO")
        self.root.geometry("200x100")
        self.root.resizable(0, 0)
        tk.Label(self.root, text=" " * 15).grid(row=0, column=0)
        tk.Button(self.root, text="Automatic Mode", command=self.__create_automatic_window).grid(row=0, column=1)
        tk.Button(self.root, text="Step Mode", command=self.__create_stepmode_window).grid(row=1, column=1)
        tk.Button(self.root, text="Edit Config", command=self.__create_config_window).grid(row=2, column=1)

    def start_ui(self):
        self.root.mainloop()

    def __create_config_window(self):
        ConfigWindow()

    def __create_automatic_window(self):
        AutomaticModeWindow()

    def __create_stepmode_window(self):
        StepModeWindow()
