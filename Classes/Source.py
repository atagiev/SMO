from Classes.Time import Time
from Classes.Request import Request
from math import log
from random import random
import config


class Source:
    def __init__(self, num, stat):
        self.__number = num
        self.__time_for_create = 0
        self.stat = stat

    def get_request(self):
        if self.__time_for_create <= Time.get_current_time():
            self.__time_for_create = self.__calculate_time_for_create()
            r = Request(self.__number, Time.get_current_time(), self.stat)
            r.created()
            Time.upd_time(self.__time_for_create)
            return r

        Time.upd_time(self.__time_for_create)
        return None

    def __calculate_time_for_create(self):
        return Time.get_current_time() + (-1/config.alf)*log(random())
