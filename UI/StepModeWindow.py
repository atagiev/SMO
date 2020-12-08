from Classes.Time import Time
from Classes.Buffer import Buffer
from Classes.Manager1 import Manager1
from Classes.Manager2 import Manager2
from Classes.Worker import Worker
from Classes.Source import Source
import config
from time import sleep
from Spy import Spy



#buffer = Buffer(config.bufferLength)
#sources = [Source(i) for i in range(config.numOfSources)]
#manager1 = Manager1(buffer, sources)
#workers = [Worker(i) for i in range(config.numOfWorkers)]
#manager2 = Manager2(buffer, workers)

#spy = Spy(sources, manager1, buffer, manager2, workers)

#while True:
 #   manager1.work()
 #   manager2.work()

    #spy.make_report()

   # Time.step()
   # sleep(1)





class StepModeWindow:
    def __init__(self):
        pass

    def open_window(self):
        pass

