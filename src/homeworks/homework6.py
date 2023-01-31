class DateError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Date:
    __days = {
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

    def __init__(self, d, m, y):
        try:
            if type(d) is not int:
                raise DateError(d, "int")
            if type(m) is not int:
                raise DateError(m, "int")
            if type(y) is not int:
                raise DateError(y, "int")
        except DateError as error:
            print(error.message)
        self.__day = d  # private so that no one can give invalis value
        self.__month = m
        self.__year = y

    def __repr__(self):
        return "{}.{}.{}".format(self.__day, self.__month, self.__year)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, count):
        try:
            if type(count) is not int:
                raise DateError(count, "int")
        except DateError as error:
            print(error.message)
        self.__year = count

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, count):
        try:
            if type(count) is not int:
                raise DateError(count, "int")
        except DateError as error:
            print(error.message)
        self.__month = count

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, count):
        try:
            if type(count) is not int:
                raise DateError(count, "int")
        except DateError as error:
            print(error.message)
        self.__day = count

    @property
    def days(self):
        return self.__days

    def __eq__(self, other):
        if not (self.__day == other.__day):
            return False
        if not (self.__month == other.__month):
            return False
        if not (self.__year == other.__year):
            return False
        return True

    def __ne__(self, other):
        return not(__eq__(self, other))

    def __lt__(self, other):
        if self.__year < other.__year:
            return True
        if self.__month < other.__month:
            return True
        if self.__day < other.__day:
            return True
        return False

    def __gt__(self, other):
        if self.__year > other.__year:
            return True
        if self.__month > other.__month:
            return True
        if self.__day > other.__day:
            return True
        return False

    def __le__(self, other):
        return __lt__(self, other) or __eq__(self, other)

    def __ge__(self, other):
        return __gt__(self, other) or __eq__(self, other)

    def add_days(self, day):
        self.__day += day
        temp = False
        while not temp:
            if self.__day <= self.__days[self.__month]:
                temp = True
            else:
                self.__day -= self.__days[self.__month]
                self.add_month(1)

    def add_month(self, m):
        self.__month += m
        self.__year += self.__month // 12
        self.__month %= 12
        # fixing the specific case
        if self.__day >= self.__days[self.__month]:
            self.__day = self.__days[self.__month]

    def add_year(self, count):
        self.__year += count

    def is_year_leap(self):
        if not self.__year % 4:
            return True
        return False

    def sub_day(self, count):
        self.__day -= count
        while self.__day < 1:
            self.__day += self.days[self.__month-1]
            self.sub_month(1)

    def sub_month(self, count):
        self. __month -= count
        while self.__month < 1:
            self.__month += 12
            self.sub_year(1)

    def sub_year(self, count):
        self.__year -= count


class TimeError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Time:
    def __init__(self, h=0, m=0, s=0):
        try:
            if type(h) is not int:
                raise TimeError(h, "int")
            if type(m) is not int:
                raise TimeError(h, "int")
            if type(s) is not int:
                raise TimeError(h, "int")
        except TimeError as error:
            print(error.message)
        self.__hour = h
        self.__minute = m
        self.__second = s
        self.__check_add = 0  # when adding hours that change the day
        self.__check_sub = 0

    def __repr__(self):
        return "{}:{}:{}".format(self.__hour,  self.__minute, self.__second)

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, count):
        try:
            if type(count) is not int:
                raise TimeError(count, "int")
        except TimeError as error:
            print(error.message)
        self.__second = count

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, count):
        try:
            if type(count) is not int:
                raise TimeError(count, "int")
        except TimeError as error:
            print(error.message)
        self.__minute = count

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, count):
        try:
            if type(count) is not int:
                raise TimeError(count, "int")
        except TimeError as error:
            print(error.message)
        self.__hour = count

    @property
    def check_add(self):
        return self.__check_add

    @check_add.setter
    def check_add(self, count):
        self.__check_add = count

    @property
    def check_sub(self):
        return self.__check_sub

    @check_sub.setter
    def check_sub(self, count):
        self.__check_sub = count

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
        self.__check_add = (self.__hour // 24)
        self.__hour %= 24
        return self.__check_add  # when adding hours that change the day

    def sub_second(self, s):
        self.__second -= s
        while self.__second < 0:
            self.sub_minute(1)
            self.__second += 60

    def sub_minute(self, m):
        self.__minute -= m
        while self.__minute < 0:
            self.sub_hour(1)
            self.__minute += 60

    def sub_hour(self, h):
        self.__hour -= h
        while self.__hour < 0:
            self.__check_sub += 1
            self.__hour += 24
        return self.__check_sub

    @staticmethod
    def sums(self, t1, t2):
        self.__hour = t1.__hour
        self.__minute = t1.__minute
        self.__second = t1.__second
        self.add_hour(t2.__hour)
        self.add_minute(t2.__minute)
        self.add_second(t2.__second)
        return self


class DateTime:
    def __init__(self, d, mounth, y, h, m, s):
        # do not need to check the exception here, as they will be checked in Date and Time classes
        self.__date = Date(d, mounth, y)
        self.__time = Time(h, m, s)

    def __repr__(self):
        return "{}  {}".format(self.__date, self.__time)

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, name):
        self.__date = name

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, name):
        self.__time = name

    def add_year(self, count):
        self.__date.add_year(count)

    def add_month(self, count):
        self.__date.add_month(count)

    def add_day(self, count):
        self.__date.add_month(count)

    def add_hour(self, count):
        are_days = self.__time.add_hour(count)
        if are_days:
            self.__date.add_days(are_days)

    def add_minute(self, count):
        self.__time.add_minute(count)
        if self.__time.check_add:
            self.__date.add_days(self.__time.check_add)

    def add_second(self, count):
        self.__time.add_second(count)
        if self.__time.check_add:
            self.__date.add_days(self.__time.check_add)

    def sub_year(self, count):
        self.__date.sub_year(count)

    def sub_month(self, count):
        self.__date.sub_year(count)

    def sub_day(self, count):
        self.__date.sub_year(count)

    def sub_second(self, count):
        self.__time.sub_second(count)
        if self.__time.check_sub:
            self.__date.sub_day(self.__time.check_sub)

    def sub_minute(self, count):
        self.__time.sub_minute(count)
        if self.__time.check_sub:
            self.__date.sub_day(self.__time.check_sub)

    def sub_hour(self, count):
        are_days = self.__time.sub_hour(count)
        if are_days:
            self.__date.sub_day(are_days)

    def __add__(self, other):
        self.__time.add_second(other.__time.second)
        self.__time.add_minute(other.__time.minute)
        self.__time.add_hour(other.__time.hour)
        self.__date.add_days(other.__date.day)
        self.__date.add_month(other.__date.month)
        self.__date.add_year(other.__date.year)
        return self

    def __sub__(self, other):
        self.__time.sub_second(other.__time.second)
        self.__time.sub_minute(other.__time.minute)
        self.__time.sub_hour(other.__time.hour)
        self.__date.sub_day(other.__date.day)
        self.__date.sub_month(other.__date.month)
        self.__date.sub_year(other.__date.year)
        return self


class CompanyError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Company:

    def __init__(self, n, f, e):
        try:
            if type(n) is not str:
                raise CompanyError(n, "str")
            if type(f) is not int:
                raise CompanyError(f, "int")
            if type(e) is not int:
                raise CompanyError(e, "int")
        except CompanyError as error:
            print(error.message)
        self.__company_name = n
        self.__founded_at = f
        self.__employes_count = e

    def __repr__(self):
        return "company-{}, founded at-{}, employes-{}".format(self.__company_name, self.__founded_at, self.__employes_count)

    @property
    def employees(self):
        return self.__employes_count

    @employees.setter
    def employees(self, name):
        try:
            if type(name) is not int:
                raise CompanyError(name, "int")
        except CompanyError as error:
            print(error.message)
        self.__employes_count = name

    @property
    def founded_at(self):
        return self.__founded_at

    def company_name(self):
        return self.__company_name


class JobError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Job:
    def __init__(self, c, s, e, p):
        try:
            if type(c) is not Company:
                raise JobError(c, "company")
            if type(s) is not Money:
                raise JobError(s, "money")
            if type(e) is not str:
                raise JobError(e, "str")
            if type(p) is not str:
                raise JobError(p, "str")
        except JobError as error:
            print(error.message)
        self.__company = c
        self.__salary = s
        self.__experience = e
        self.__position = p

    def __repr__(self):
        return "comapny-{},salary-{},experience-{},position-{}".format(self.__company, self.__salary, self.__experience, self.__position)

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, name):
        try:
            if type(name) is not Company:
                raise JobError(name, "company")
        except JobError as error:
            print(error.message)
        self.__company = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, name):
        try:
            if type(name) is not int:
                raise JobError(name, "int")
        except JobError as error:
            print(error.message)
        self.__salary = name

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, name):
        try:
            if type(name) is not str:
                raise JobError(name, "str")
        except JobError as error:
            print(error.message)
        self.__experience = name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, name):
        try:
            if type(name) is not str:
                raise JobError(name, "str")
        except JobError as error:
            print(error.message)
        self.__position = name

    def change_salary(self, change):
        self.__salary = change

    def change_experience(self, change):
        self.__experience = change

    def change_position(self, change):
        self.__position = change


class PersonError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Person:
    def __init__(self, n, s, g, age, a, f, j):
        try:
            if type(n) is not str:
                raise PersonError(n, "str")
            if type(s) is not str:
                raise PersonError(s, "str")
            if type(g) is not str:
                raise PersonError(g, "str")
            if type(age) is not int:
                raise PersonError(age, "int")
            if type(a) is not str:
                raise PersonError(a, "str")
            if type(f) is not list:
                raise PersonError(f, "list")
        except PersonError as error:
            print(error.message)
        self.__name = n
        self.__surname = s
        self.__gender = g
        self.__age = age
        self.__address = a
        self.__friends = f
        self.__jobs = j

    def __repr__(self):
        return "name-{},surname-{},gender-{},age-{},address-{},friends-{},job-{}".format(self.__name, self.__surname, self.__gender, self.__age, self.__address, self.__friends, self.__jobs)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        try:
            if type(n) is not str:
                raise PersonError(n, "str")
        except PersonError as error:
            print(error.message)
        self.__name = n

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, name):
        try:
            if type(name) is not str:
                raise PersonError(name, "str")
        except PersonError as error:
            print(error.message)
        self.__surname = name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, name):
        try:
            if type(name) is not str:
                raise PersonError(name, "str")
        except PersonError as error:
            print(error.message)
        self.__gender = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, name):
        try:
            if type(name) is not int:
                raise PersonError(name, "int")
        except PersonError as error:
            print(error.message)
        self.__age = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, name):
        try:
            if type(name) is not int:
                raise PersonError(name, "int")
        except PersonError as error:
            print(error.message)
        self.__address = name

    @property
    def friends(self):
        return self.__friends

    @friends.setter
    def friends(self, name):
        try:
            if type(name) is not list:
                raise PersonError(name, "list")
        except PersonError as error:
            print(error.message)
        self.__friends = name

    @property
    def jobs(self):
        return self.__jobs

    @jobs.setter
    def jobs(self, name):
        try:
            if type(name) is not list:
                raise PersonError(name, "list")
        except PersonError as error:
            print(error.message)
        self.__jobs = name

    def add_friend(self, other):
        self.__friends.append(other)
        other.__friends.append(self)

    def remove_friend(self, other):
        self.__friends.remove(other)
        other.__friends.remove(self)

    def add_job(self, job):
        self.__jobs.append(job)

    def remove_job(self, job):
        self.__jobs.remove(job)

    def display_job(self):
        print(self.__jobs)


class DoctorError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Doctor(Person):
    def __init__(self, n, s, g, age, a, f, j, dep, prof, pat, sal):
        super().__init__(n, s, g, age, a, f, j)
        try:
            if type(dep) is not str:
                raise DoctorError(dep, "str")
            if type(prof) is not str:
                raise DoctorError(prof, "str")
            if type(pat) is not str:
                raise DoctorError(pat, "str")
            if type(sal) is not Money:
                raise DoctorError(sal, "money")
        except DoctorError as error:
            print(error.message)

        self.__department = dep  # string
        self.__profession = prof  # string
        self.__patronymic = pat  # string
        self. __salary = sal  # integer

    def __repr__(self):
        return "name-{},surname-{},gender-{},age-{},address-{},friends-{},job-{},department-{}, profession-{}, patronymic-{}, salary-{}".format(self.__name, self.__surname, self.__gender, self.__age, self.__address, self.__friends, self.__jobs, self.__department, self.__profession, self.__patronymic, self.__salary)

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, name):
        try:
            if type(name) is not str:
                raise DoctorError(name, "str")
        except DoctorError as error:
            print(error.message)
        self.__department = name

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, name):
        try:
            if type(name) is not str:
                raise DoctorError(name, "str")
        except DoctorError as error:
            print(error.message)
        self.__profession = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, name):
        try:
            if type(name) is not str:
                raise DoctorError(name, "str")
        except DoctorError as error:
            print(error.message)
        self.__patronymic = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, name):
        try:
            if type(name) is not Money:
                raise DoctorError(name, "money")
        except DoctorError as error:
            print(error.message)
        self.__salary = name


class MoneyError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Money:
    exchange = {
        'AMD': 1,
        "RUB": 5.8,
        "USD": 400,
        "EUR": 430
    }

    def __init__(self, a, c):
        try:
            if c not in Money.exchange.keys():
                raise MoneyError(c, "exchange key")
            if type(a) is not int and type(a) is not float:
                raise MoneyError(a, "int or float")
        except MoneyError as error:
            print(error.message)
        self.__ammount = a
        self.__currency = c

    def __repr__(self):
        return "{} {}".format(self.__ammount, self.__currency)

    @property
    def ammount(self):
        return self.__ammount

    @ammount.setter
    def ammount(self, name):
        try:
            if type(name) is not int and type(name) is not float:
                raise MoneyError(name, "int or float")
        except MoneyError as error:
            print(error.message)
        self.__ammount = name

    @property
    def currecny(self):
        return self.__currency

    @currecny.setter
    def currecny(self, name):
        try:
            if name not in Money.exchange.keys():
                raise MoneyError(name, "exchange key")
        except MoneyError as error:
            print(error.message)
        self.__currency = name

    def conversation(self, curr):
        try:
            if curr not in Money.exchange.keys():
                raise MoneyError(curr, "exchange key")
        except MoneyError as error:
            print(error.message)
        exchange_rate = self.exchange[self.__currency] / self.exchange[curr]
        return Money(self.__ammount * exchange_rate, curr)

    def __add__(self, other):
        tem = other.conversation(self.__currency)
        return Money(self.__ammount + tem.__ammount, self.__currency)

    def __sub__(self, other):
        tem = other.conversation(self.__currency)
        return Money(self.__ammount - tem.__ammount, self.__currency)

    def __truediv__(self, other):
        tem = other.conversation(self.__currency)
        return Money(self.__ammount / tem.__ammount, self.__currency)

    def __eq__(self, other):
        return self.__ammount == other.conversation(self.__currency).__ammount

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__ammount < other.conversation(self.__currency).__ammount

    def __gt__(self, other):
        return self.__ammount > other.conversation(self.__currency).__ammount

    def __le__(self, other):
        return self.__ammount <= other.conversation(self.__currency).__ammount

    def __ge__(self, other):
        return self.__ammount >= other.conversation(self.__currency).__ammount


class RangeError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class MyRange:
    def __init__(self, c, e, s):
        try:
            if type(c) is not int and type(c) is not float:
                raise RangeError(c, "int or float")
            if type(e) is not int and type(e) is not float:
                raise RangeError(e, "int or float")
            if type(s) is not int and type(s) is not float:
                raise RangeError(s, "int or float")
        except RangeError as error:
            print(error.message)
        self.__current = c
        self.__end = e
        self.__step = s
        self.__first = self.__current - self.__step
        self.__reverse = []

    def __repr__(self):
        return "current - {}, end - {}, step - {}".format(self.__current, self.__end, self.__step)

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, curr):
        try:
            if type(curr) is not int and type(curr) is not float:
                raise RangeError(curr, "int or float")
        except RangeError as error:
            print(error.message)
        self.__current = curr

    @property
    def endd(self):
        return self.__end

    @endd.setter
    def endd(self, end):
        try:
            if type(end) is not int and type(end) is not float:
                raise RangeError(end, "int or float")
        except RangeError as error:
            print(error.message)
        self.__current = end

    @property
    def step(self):
        return self.__current

    @step.setter
    def step(self, step):
        try:
            if type(step) is not int and type(step) is not float:
                raise RangeError(step, "int or float")
        except RangeError as error:
            print(error.message)
        self.__current = step

    def __iter__(self):
        self.__first = self.__current - self.__step
        return self

    def __next__(self):
        if self.__first+self.__step < self.__end:
            self.__first += self.__step
            return self.__first
        else:
            raise StopIteration

    def __len__(self):
        p = self.__end - self.__current
        if self.__step < 0:
            p *= -1
        ll = ""
        for i in range(p):
            ll = ll + "h"
        return len(ll)

    def __getitem__(self, index):
        for i in range(index+1):
            self.__next__()
        return self.__first

    def __reversed__(self):
        for i in range(self.__end, self.__current, -1*self.__step):
            self.__reverse.append(i)
        return self.__reverse


class CityError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class City:
    def __init__(self, n, m, p, lang):
        try:
            if type(n) is not str:
                raise CityError(n, "str")
            if type(m) is not Person:
                raise CityError(m, "Person")
            if type(p) is not int:
                raise CityError(p, "int")
            if type(lang) is not str:
                raise CityError(lang, "str")
        except CityError as error:
            print(error.message)
        self.__name = n  # string
        self.__mayor = m  # person class
        self.__population = p  # integer
        self.__language = lang  # string

    def __repr__(self):
        return "name-{}, mayor-{}, population-{}, language-{}".format(self.__name, self.__mayor, self.__population, self.__language)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, names):
        try:
            if type(names) is not str:
                raise CityError(names, "str")
        except CityError as error:
            print(error.message)
        self.__name = names

    @property
    def mayor(self):
        return self.__mayor

    @mayor.setter
    def mayor(self, name):
        try:
            if type(name) is not Person:
                raise CityError(name, "Person")
        except CityError as error:
            print(error.message)
        self.__mayor = name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, name):
        try:
            if type(name) is not int:
                raise CityError(name, "int")
        except CityError as error:
            print(error.message)
        self.__population = name

    @property
    def language(self):
        return self.__language


class UniversityError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class University:
    def __init__(self, n, f, r, c):
        try:
            if type(n) is not str:
                raise UniversityError(n, "str")
            if type(f) is not Date:
                raise UniversityError(f, "Date")
            if type(r) is not Person:
                raise UniversityError(r, "Person")
            if type(c) is not City:
                raise UniversityError(c, "City")
        except UniversityError as error:
            print(error.message)
        self.__name = n  # string
        self.__founded_at = f  # date class
        self.__rector = r  # person class
        self.__city = c  # city class

    def __repr__(self):
        return "name-{}, founded_at-{}, rector - {}, city-{}".format(self.__name, self.__founded_at, self.__rector, self.__city)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nam):
        try:
            if type(nam) is not str:
                raise UniversityError(nam, "str")
        except UniversityError as error:
            print(error.message)
        self.__name = nam

    @property
    def founded(self):
        return self.__founded_at

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, name):
        try:
            if type(name) is not Person:
                raise UniversityError(name, "Person")
        except UniversityError as error:
            print(error.message)
        self.__rector = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, name):
        try:
            if type(name) is not City:
                raise UniversityError(name, "City")
        except UniversityError as error:
            print(error.message)
        self.__city = name


class TeacherError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Teacher(Person):
    def __init__(self, n, s, g, age, a, f, j, uni, fac, exp, start, subj, sal):
        super().__init__(n, s, g, age, a, f, j)
        try:
            if type(fac) is not str:
                raise TeacherError(fac, "str")
            if type(exp) is not int:
                raise TeacherError(exp, "int")
            if type(start) is not Date:
                raise TeacherError(start, "Date")
            if type(subj) is not str:
                raise TeacherError(subj, "str")
            if type(sal) is not Money:
                raise TeacherError(sal, "money")
        except TeacherError as error:
            print(error.message)
        self.__university = uni
        self.__faculty = fac  # string
        self.__experience = exp  # integer
        self.__start_work_at = start  # date class
        self.__subject = subj  # string
        self. __salary = sal  # money

    def __repr__(self):
        return "name-{},surname-{},gender-{},age-{},address-{},friends-{},job-{},university-{}, faculty-{}, experience-{}, start_work_at-{}, subject -{}, salary-{}".format(self.__name, self.__surname, self.__gender, self.__age, self.__address, self.__friends, self.__jobs, self.__university, self.__faculty, self.__experience, self.__start_work_at, self.__subject, self.__salary)

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, name):
        self.__university = name

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, name):
        try:
            if type(name) is not str:
                raise TeacherError(name, "str")
        except TeacherError as error:
            print(error.message)
        self.__faculty = name

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, name):
        try:
            if type(name) is not int or name < 0:
                raise TeacherError(name, "positive int")
        except TeacherError as error:
            print(error.message)
        self.__experience = name

    @property
    def start_work_at(self):
        return self.__start_work_at

    @start_work_at.setter
    def start_work_at(self, name):
        try:
            if type(name) is not Date:
                raise TeacherError(name, "Date")
        except TeacherError as error:
            print(error.message)
        self.__start_work_at = name

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, name):
        try:
            if type(name) is not str:
                raise TeacherError(name, "str")
        except TeacherError as error:
            print(error.message)
        self.__subject = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, name):
        try:
            if type(name) is not Money:
                raise TeacherError(name, "Money")
        except TeacherError as error:
            print(error.message)
        self.__salary = name


class StudentError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Student(Person):
    def __init__(self, n, s, g, age, a, f, j, uni, fac, c, start):
        super().__init__(n, s, g, age, a, f, j)
        try:
            if type(fac) is not str:
                raise StudentError(fac, "str")
            if type(c) is not int:
                raise StudentError(c, "int")
            if type(start) is not Date:
                raise StudentError(start, "Date")
        except StudentError as error:
            print(error.message)
        self.__university = uni
        self.__faculty = fac  # string
        self.__course = c  # integer
        self.__start_at = start  # date class

    def __repr__(self):
        return "name-{},surname-{},gender-{},age-{},address-{},friends-{},job-{},uni-{},faculty-{},course-{},start-{}".format(self.name, self.surname, self.gender, self.age, self.address, self.friends, self.jobs, self.university, self.faculty, self.__course, self.__start_at)

    @property
    def university(self):
        print("getter")
        return self.__university

    @university.setter
    def university(self, name):
        print("setter")
        self.__university = name

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, name):
        try:
            if type(name) is not str:
                raise StudentError(name, "str")
        except StudentError as error:
            print(error.message)
        self.__faculty = name

    @property
    def course(self):
        return self.course

    @course.setter
    def course(self, name):
        try:
            if type(name) is not int or name < 0:
                raise StudentError(name, "positive int")
        except StudentError as error:
            print(error.message)
        self.__course = name

    @property
    def start_at(self):
        return self.start_at

#
# def call_counter(func):
#     def helper(x):
#         helper.calls += 1
#         return func(x)
#     helper.calls = 0
#     return helper
#
#
# @call_counter
# def succ(x):
#     return x + 1


date = Date(31, 1, 2000)
print("specific case\n", date)
date.add_month(1)
print(date)
print("----------")

dt = DateTime(31, 1, 2023, 0, 38, 5)
print("Date&Time cases\n", dt)
dt.add_year(3)
print(dt)
dt.add_month(15)
print(dt)
dt.add_day(5)
print(dt)
dt.add_hour(25)
print(dt)
dt.sub_second(6)
print("sub second", dt)
dt.add_minute(5)
print(dt)
kk = DateTime(3, 5, 1999, 7, 20, 45)
print("__add__", dt+kk, "\n-----------")


dt1 = DateTime(31, 1, 2020, 23, 59, 59)
dt1.add_second(2)
print("special case", dt1)
dt1.sub_second(2)
print("special case", dt1, "\n-----------")

aca = Company("ACA", 2010, 100)
print("Company\n", aca, "\n-----------")

manager = Job(aca, 1000, 1, "junior")
lawer = Job("law", 900, 2, "middle")
print(manager)
manager.change_salary(1500)
print("job\n", manager, "\n", lawer, "\n-----------")

student1 = Student("Emmy", "Williams", "Female", 25, "Burbank", [], [manager], "Yell", "Managment", 3, Date(3, 8, 2020))
print("student\n", student1,)
tempp = student1.university
print(tempp)
student1.university = "AUA"

print("-----------\n Person")
person1 = Person("Emmy", "Williams", "Female", 25, "Burbank 35", [], [manager])
person2 = Person("John", "Gates", "Male", 43, "Wolf street", [], [lawer])
print(person1)
print(person2)
person1.add_friend(person2)
person2.remove_friend(person1)
print(person1)
print(person2)
person2.add_job(manager)
print(aca)
person2.display_job()

print("----------\nMoney")
dram = Money(1000, 'AMD')
dollar = Money(3, "USD")
money1 = dram+dollar
print(money1)
print(dram.conversation("RUB"))
print(dollar)
rubl = Money(500, "RUB")
money2 = rubl - dollar
print(money2)

print("--------\nMy Range")
range1 = MyRange(1, 10,  2)
print("iter-")
for x in range1:
    print(x)
print("\n")
range2 = MyRange(-6, 3, 3)
print("next-\n", range2.__next__())
print(range2.__next__())
print(range2.__next__())
print("length", len(range2))
range3 = MyRange(5, 15, 3)
print("getitem", range3[3])
print("reversed-", range3.__reversed__())


def counter(f):
    def counted(n):
        counted.call_count += 1
        print("the function was called {} times".format(counted.call_count))
        return f(n)
    counted.call_count = 0
    return counted


@counter
def the_function(n):
    print("the input number is", n)


num = 7
the_function(num)
the_function(num)
