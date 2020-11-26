from Classes.Time import Time
from Classes.Request import Request
from math import exp
from random import random
import config


class Source:
    def __init__(self, num):
        self.__number = num
        self.__time_for_create = 0

    def get_request(self):
        if self.__time_for_create <= Time.get_current_time():
            self.__time_for_create = self.__calculate_time_for_create()
            r = Request(self.__number, Time.get_current_time())
            r.created()
            return r

        return None

    def __calculate_time_for_create(self):
        return Time.get_current_time() + config.alf * exp(int(random() * -config.alf))
