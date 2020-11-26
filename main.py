from Classes.Time import Time
from Classes.Buffer import Buffer
from Classes.Manager1 import Manager1
from Classes.Manager2 import Manager2
from Classes.Worker import Worker
from Classes.Source import Source
import config
from time import sleep
from Spy import Spy

# 21.	ИБ  ИЗ1  ПЗ1  Д10З1  Д10О3  Д2П1  Д2Б3  ОР2  ОД3

# ИЗ1	—	пуассоновский	для	бесконечных,
# ПЗ1 — экспоненциальный;
# Д1ОЗ1 — по кольцу;
# Д1ОО3 — самая старая в буфере;
# Д2П1 — приоритет по номеру прибора;
# Д2Б3 — по кольцу
# ОР2 — графики по значениям параметров;
# ОД3 — временные диаграммы, текущее состояние.


if __name__ == '__main__':

    buffer = Buffer(config.bufferLength)
    sources = [Source(i) for i in range(config.numOfSources)]
    manager1 = Manager1(buffer, sources)
    workers = [Worker(i) for i in range(config.numOfWorkers)]
    manager2 = Manager2(buffer, workers)

    spy = Spy(sources, manager1, buffer, manager2, workers)

    while True:
        manager1.work()
        manager2.work()

        spy.make_report()

        Time.step()
        sleep(1)
