import config


class StatCollector:
    def __init__(self):
        self.sources_created = [0] * config.numOfSources
        self.sources_denied = [0] * config.numOfSources
        self.sources_completed = [0] * config.numOfSources
        self.workers_worked = [0] * config.numOfWorkers
        self.sources_wait_time = [0] * config.numOfSources
        self.sources_all_time = [0] * config.numOfSources
        self.sources_work_time = [0] * config.numOfSources
        self.workers_last_request_time = [0] * config.numOfWorkers

    def created(self, i):
        self.sources_created[i] += 1

    def denied(self, i):
        self.sources_denied[i] += 1

    def completed(self, i):
        self.sources_completed[i] += 1

    def add_worker_time(self, num, time):
        self.workers_last_request_time[num] = time

    def add_worker_time2(self, num, time):
        self.workers_worked[num] += time - self.workers_last_request_time[num]

    def add_wait_time(self, num, time):
        self.sources_wait_time[num] += time

    def add_all_time(self, num, time):
        self.sources_all_time[num] += time

    def add_work_time(self, num, time):
        self.sources_work_time[num] += time
