from time import time, localtime, sleep


class Clock(object):


    def __init__(self, hour = 0, minute = 0, second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)