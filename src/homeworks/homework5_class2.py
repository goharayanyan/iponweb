class Date:
    def __init__(self, d, m, y):
        self.__day = d  # private so that no one can give invalis value
        self.__month = m
        self.__year = y

    def __repr__(self):
        return "{}.{}.{}".format(self.__day, self.__month, self.__year)

    def add_days(self, day):
        d = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        self.__day += day
        temp = False
        while not temp:
            if self.__day <= d[self.__month]:
                temp = True
            else:
                self.__day -= d[self.__month]
                self.add_month(1)

    def add_month(self, m):
        self.__month += m
        self.__year += m // 12
        self.__month %= 12

    def add_year(self, count):
        self.__year += count

    def is_year_leap(self):
        if not self.__year % 4:
            return True
        return False


class Time:
    def __init__(self, s=0, m=0, h=0):
        self.__second = s
        self.__minute = m
        self.__hour = h

    def __repr__(self):
        return "{}:{}:{}".format(self.__second, self.__minute, self.__hour)

    def add_second(self, s):
        self.__second += s
        self.add_minute(self.__second // 60)
        self.__second %= 60

    def add_minute(self, m):
        self.__minute += m
        self.add_hour(self.__minute // 60)
        self.__minute %= 60

    def add_hour(self, h):
        self.__hour += h
        self.__hour %= 24

    @staticmethod
    def sums(self, t1, t2):
        self.__hour = t1.__hour
        self.__minute = t1.__minute
        self.__second = t1.__second
        self.add_hour(t2.__hour)
        self.add_minute(t2.__minute)
        self.add_second(t2.__second)
        return self


date1 = Date(23, 2, 2023)
print(date1)
date1.add_month(38)
print(date1)
date1.add_days(30)
print(date1)
print(date1.is_year_leap())

time1 = Time(25, 46, 22)
time1.add_minute(12)
print(time1)
time2 = Time(45, 48, 4)
time3 = Time()
print(time3.sums(time3, time1, time2))


d = Date(31,1,2000)
d.add_month(1)
print(d)