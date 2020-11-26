from Classes.Buffer import Buffer
from Classes.Manager1 import Manager1
from Classes.Manager2 import Manager2
from Classes.Time import Time


class Spy:
    def __init__(self, sources, manager1: Manager1, buffer: Buffer, manager2: Manager2, workers):
        self.sources = sources
        self.manager1 = manager1
        self.buffer = buffer
        self.manager2 = manager2
        self.workers = workers

    def __make_sources_report(self):
        for i in self.sources:
            print("Source №" + str(i._Source__number) + " next request will be created at " + str(
                i._Source__time_for_create))

    def __make_buffer_report(self):
        c = self.buffer._Buffer__buffer_length - self.buffer._Buffer__buffer.count(None)
        print("\nBuffer count " + str(c) + " pointer1 " + str(self.buffer._Buffer__pointer1) + " pointer2 " + str(
            self.buffer._Buffer__pointer2))

        for i in self.buffer._Buffer__buffer:
            if i is None:
                print("None")
            else:
                print(i.get_id())

    def __make_workers_report(self):
        print("\nWorkers:")
        for i in self.workers:
            print("Worker №" + str(i._Worker__number)+" is available " + str(i.is_available()) + ("" if i.is_available() else " release time " + str(i._Worker__time_of_release)))

    def make_report(self):
        print("\nREPORT          TIME = " + str(Time.get_current_time()))
        self.__make_sources_report()
        self.__make_buffer_report()
        self.__make_workers_report()
        print("END OF REPORT\n")
        print("-"*100 + "\n")
