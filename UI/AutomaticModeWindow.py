import config
from Classes.StatCollector import StatCollector
from Classes.Time import Time
from Classes.Buffer import Buffer
from Classes.Manager1 import Manager1
from Classes.Manager2 import Manager2
from Classes.Worker import Worker
from Classes.Source import Source
import tkinter as tk


class AutomaticModeWindow:
    def __init__(self):
        self.stat = StatCollector()
        self.__work_system()
        self.window = tk.Toplevel()
        self.window.grab_set()
        self.window.title("Automatic mode")
        self.__create_ui()

    def __work_system(self):
        buffer = Buffer(config.bufferLength)
        sources = [Source(i, self.stat) for i in range(config.numOfSources)]
        manager1 = Manager1(buffer, sources)
        workers = [Worker(i) for i in range(config.numOfWorkers)]
        manager2 = Manager2(buffer, workers)

        for i in range(config.auto_mode_steps):
            manager1.work()
            manager2.work()
            Time.step()

    def __create_ui(self):
        tk.Label(self.window, text="Sources").grid(row=0, column=0)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Имя')
        e0.grid(row=1, column=0)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Создано')
        e0.grid(row=1, column=1)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Выполнено')
        e0.grid(row=1, column=2)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Отклонено')
        e0.grid(row=1, column=3)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Ср. время в системе')
        e0.grid(row=1, column=4)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Ср. время ожидания')
        e0.grid(row=1, column=5)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Ср. время обработки')
        e0.grid(row=1, column=6)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Вероятность отказа')
        e0.grid(row=1, column=7)

        for i in range(2, 2+config.numOfSources):
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set("Source " + str(i-2))
            e0.grid(row=i, column=0)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(self.stat.sources_created[i-2])
            e0.grid(row=i, column=1)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(self.stat.sources_completed[i-2])
            e0.grid(row=i, column=2)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(self.stat.sources_denied[i - 2])
            e0.grid(row=i, column=3)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(self.stat.sources_all_time[i - 2]/self.stat.sources_completed[i-2])[0:4])
            e0.grid(row=i, column=4)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(self.stat.sources_wait_time[i-2]/(self.stat.sources_completed[i-2]+self.stat.sources_denied[i-2]))[0:4])
            e0.grid(row=i, column=5)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(self.stat.sources_work_time[i-2]/self.stat.sources_completed[i-2])[0:4])
            e0.grid(row=i, column=6)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(self.stat.sources_denied[i - 2] / self.stat.sources_created[i - 2] * 100)[0:4] + "%")
            e0.grid(row=i, column=7)

        tk.Label(self.window, text="Devices").grid(row=2+config.numOfSources, column=0)

        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set("Имя")
        e0.grid(row=config.numOfSources+3, column=0)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set("Коэф. использования")
        e0.grid(row=config.numOfSources+3, column=1)
        for i in range(config.numOfSources+4, config.numOfSources+4+config.numOfWorkers):
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set("Device "+str(i - config.numOfSources - 4))
            e0.grid(row=i, column=0)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(self.stat.workers_worked[i - config.numOfSources - 4]/Time.get_current_time())
            e0.grid(row=i, column=1)

