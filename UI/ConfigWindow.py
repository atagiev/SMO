import tkinter as tk
import config


class ConfigWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.grab_set()
        self.window.title("Edit Config")
        self.__create_ui()

    def __save(self):
        config.bufferLength = int(self.__bl.get())
        config.numOfSources = int(self.__ns.get())
        config.numOfWorkers = int(self.__nw.get())
        config.alf = float(self.__sc.get())
        config.lam = float(self.__wc.get())
        config.auto_mode_steps = int(self.__au.get())

    def __create_ui(self):
        self.__bl = tk.StringVar()
        self.__ns = tk.StringVar()
        self.__nw = tk.StringVar()
        self.__sc = tk.StringVar()
        self.__wc = tk.StringVar()
        self.__au = tk.StringVar()

        tk.Label(self.window, text="Buffer length").grid(row=0, column=0)
        tk.Label(self.window, text="Sources").grid(row=1, column=0)
        tk.Label(self.window, text="Workers").grid(row=2, column=0)
        tk.Label(self.window, text="Sources coef").grid(row=3, column=0)
        tk.Label(self.window, text="Workers coef").grid(row=4, column=0)
        tk.Label(self.window, text="Steps in automode").grid(row=5, column=0)
        bl = tk.Entry(self.window, textvariable=self.__bl)
        bl.insert(0, config.bufferLength)
        bl.grid(row=0, column=1)
        ns = tk.Entry(self.window, textvariable=self.__ns)
        ns.insert(0, config.numOfSources)
        ns.grid(row=1, column=1)
        nw = tk.Entry(self.window, textvariable=self.__nw)
        nw.insert(0, config.numOfWorkers)
        nw.grid(row=2, column=1)
        sc = tk.Entry(self.window, textvariable=self.__sc)
        sc.insert(0, config.alf)
        sc.grid(row=3, column=1)
        wc = tk.Entry(self.window, textvariable=self.__wc)
        wc.insert(0, config.lam)
        wc.grid(row=4, column=1)
        au = tk.Entry(self.window, textvariable=self.__au)
        au.insert(0, config.auto_mode_steps)
        au.grid(row=5, column=1)
        tk.Button(self.window, text="Save", command=self.__save).grid(row=6, column=0, padx=5, pady=5)
