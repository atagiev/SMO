class Manager1:

    def __init__(self, buffer, sources):
        self.__requests = []
        self.__buffer = buffer
        self.__sources = sources

    def __collect_requests(self):
        for source in self.__sources:
            request = source.get_request()
            if request is not None:
                self.__requests.append(request)

    def __fill_buffer(self):
        for request in self.__requests:
            self.__buffer.add_request(request)
        self.__requests = []

    def work(self):
        self.__collect_requests()
        self.__fill_buffer()
