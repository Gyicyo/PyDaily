from time import localtime,time

class Clock:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def now(cls):
        t = localtime(time())
        return cls(t.tm_hour, t.tm_min, t.tm_sec)

c = Clock.now()
print(c.hour, c.minute, c.second)