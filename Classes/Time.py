class Time:
    __time = 0

    @staticmethod
    def get_current_time():
        return Time.__time

    @staticmethod
    def update_time(time):
        Time.__time += time

    @staticmethod
    def step():
        Time.update_time(1)
