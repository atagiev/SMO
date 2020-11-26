class Request:
    def __init__(self, num_of_source, create_time):
        self.__numOfSource = num_of_source
        self.__time = create_time

    def get_time(self):
        return self.__time

    def get_id(self):
        return str(self.__numOfSource)+","+str(self.__time)

    def created(self):
        print("Запрос " + self.get_id() + " создан источником " + str(self.__numOfSource))

    def in_buffer(self):
        print("Запрос " + self.get_id() + " помещен в буфер")

    def leave_buffer(self):
        print("Запрос " + self.get_id() + " покинул буфер")

    def in_worker(self, num):
        print("Запрос " + self.get_id() + " попал в обработку прибором " + str(num))

    def leave_worker(self, num):
        print("Запрос " + self.get_id() + " успешно обработан прибором " + str(num))

    def deny_buffer(self):
        print("Запрос " + self.get_id() + " выброшен из буфера")
