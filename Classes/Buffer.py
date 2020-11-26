class Buffer:
    def __init__(self, buffer_length):
        self.__buffer_length = buffer_length
        self.__buffer = [None] * self.__buffer_length

        self.__pointer1 = 0
        self.__pointer2 = 0

    def add_request(self, request):
        added = False
        for i in range(self.__pointer1, self.__buffer_length):
            if self.__buffer[i] is None:
                self.__pointer1 = i + 1
                self.__buffer[i] = request
                added = True
                break

        if added and self.__pointer1 == self.__buffer_length:
            self.__pointer1 = 0

        if not added:
            for i in range(0, self.__pointer1):
                if self.__buffer[i] is None:
                    self.__pointer1 = i + 1
                    self.__buffer[i] = request
                    added = True
                    break

        if added:
            request.in_buffer()
        else:
            self.__deny_request(request)

    def __deny_request(self, request):
        oldest = 0
        for i in range(1, self.__buffer_length):
            if self.__buffer[i].get_time() < self.__buffer[oldest].get_time():
                oldest = i

        request.in_buffer()
        self.__buffer[oldest].deny_buffer()
        self.__buffer[oldest] = request

    def get_request(self):
        for i in range(self.__pointer2, self.__buffer_length):
            if self.__buffer[i] is not None:
                r = self.__buffer[i]
                self.__buffer[i] = None
                if i + 1 == self.__buffer_length:
                    self.__pointer2 = 0
                else:
                    self.__pointer2 = i + 1

                r.leave_buffer()
                return r

        for i in range(0, self.__pointer2):
            if self.__buffer[i] is not None:
                r = self.__buffer[i]
                self.__buffer[i] = None
                self.__pointer2 = i + 1

                r.leave_buffer()
                return r

        return None
