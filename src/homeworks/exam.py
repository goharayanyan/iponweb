from datetime import timedelta
import datetime


class PatientError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Patient:
    def __init__(self, n, s, a, g):
        try:
            if type(n) is not str:
                raise PatientError(n, "str")
            if type(s) is not str:
                raise PatientError(s, "str")
            if type(a) is not int or a <= 18 or a >= 100:
                raise PatientError(a, "int")
            if not(g == "F" or g == "M"):
                raise PatientError(g, "gender")
        except PatientError as error:
            print(error.message)
        self.name = n
        self.surname = s
        self.age = a
        self.gender = g

    def __repr__(self):
        return "{} {} - {},{} years old".format(self.name, self.surname, self.gender, self.age)

    def __ne__(self, other):
        if self.name == other.name and self.surname == other.surname and self.age == other.age and self.gender == other.gender:
            return False
        else:
            return True


class DoctorError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Doctor:
    def __init__(self, n, s, sc):
        try:
            if type(n) is not str:
                raise DoctorError(n, "str")
            if type(s) is not str:
                raise DoctorError(s, "str")
            if type(sc) is not dict:
                raise DoctorError(sc, "dict")
        except DoctorError as error:
            print(error.message)
        self.name = n
        self.surname = s
        self.schedule = sc
        self.work_hours = {}

    def __repr__(self):
        return "Doctor {} {}, schedule {}".format(self.name, self.surname, self.schedule)

    def register_patient(self, patient, dat):
        if self.is_registered(patient):
            print("Patient {} already registered".format(patient))
        elif not self.is_free(dat):
            print("DateTime {} is already taken".format(dat))
        else:
            if dat.day not in self.work_hours.keys():
                self.work_hours[dat.day] = 0.5
            elif self.work_hours[dat.day] == 8:
                print(" o=no free time in this day")
            else:
                self.work_hours[dat.day] += 0.5
            self.schedule[patient] = dat
            print("Patient {} successfully registered at {}".format(patient, dat))

    def is_free(self, date):
        res = True
        for i in self.schedule.keys():
            if date > i:
                if (i+timedelta(minutes=30)) > date:
                    res = False
            if date < i:
                if(date + timedelta(minutes=30)) > i:
                    res = False
        return res

    def is_registered(self, patient):
        if patient in self.schedule.values():
            return True
        else:
            return False


class BuyError(Exception):
    def __init__(self):

        self.message = "There is not enough procduct"


class ProductError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Product:
    def __init__(self, p, id, q):
        try:
            if type(p) is not int:
                raise ProductError(p, "int")
            if type(id) is not int:
                raise ProductError(id, "int")
            if type(q) is not int:
                raise ProductError(q, "int")
        except ProductError as error:
            print(error.message)
        self.price = p
        self.id = id
        self.quantity = q

    def __repr__(self):
        return "price - {}, id-{}, qunatity - {}".format(self.price, self.id, self.quantity)

    def buy(self, count):
        try:
            if count > self.quantity:
                raise BuyError
            else:
                self.quantity -= count
        except BuyError as error:
            print(error.message)


class InventoryError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Inventory:
    def __init__(self, l):
        try:
            if type(l) is not list:
                raise InventoryError(l, "list")
        except InventoryError as error:
            print(error.message)
        self.list = l

    def __repr__(self):
        return "The list of products - {}".format(self.list)

    def get_by_id(self, id):
        for i in self.list:
            if i.id == id:
                return i
        else:
            return "No element with this ID"

    def sum_of_products(self):
        sums = 0
        for i in self.list:
            sums += i.quantity
        return sums


class PassangerError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Passanger:
    def __init__(self, n, c, r):
        try:
            if type(n) is not str:
                raise PassangerError(n, "str")
            if type(c) is not str:
                raise PassangerError(c, "str")
            if type(r) is not dict:
                raise PassangerError(r, "dict")
        except PassangerError as error:
            print(error.message)
        self.__name = n
        self.__city = c
        self.__rooms = r

    def __repr__(self):
        return "Passanger name - {}, city - {}, rooms - {}".format(self.__name, self.__city, self.__rooms)

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def rooms(self):
        return self.__rooms


class HotelError(Exception):
    def __init__(self, value, typpe):
        self.type = typpe
        self.value = value
        self.message = "{} is not a {}".format(self.value, self.type)


class Hotel:
    def __init__(self, c, p, s, d):
        try:
            if type(c) is not str:
                raise HotelError(c, "str")
            if type(p) is not int:
                raise HotelError(p, "int")
            if type(s) is not int:
                raise HotelError(s, "int")
            if type(d) is not int:
                raise HotelError(d, "int")
        except HotelError as error:
            print(error.message)
        self.__city = c
        self.__rooms = {
            "penthouse": p,
            "single": s,
            "double": d
        }

    def __repr__(self):
        return "city - {}, rooms - {}".format(self.__city, self.__rooms)

    @property
    def city(self):
        return self.__city

    def free_rooms_list(self, room_type):
        return self.__rooms[room_type]

    def reserve_rooms(self, room_type, count):
        if self.__rooms[room_type] > count:
            self.__rooms[room_type] -= count
            return self.__rooms[room_type]
        else:
            print("there is not so many free rooms")

    def reserve_roomss(self, passanger):
        res = True
        for i in passanger.rooms.keys():
            if self.__rooms[i] < passanger.rooms[i]:
                print("there is not so many free rooms")
                res = False
        if res:
            for j in passanger.rooms.keys():
                self.__rooms[j] -= passanger.rooms[j]
            return self.__rooms[j]


pat1 = Patient("Gohar", "Ayanyan", 20, "F")
pat2 = Patient("hjds", "vbpod", 20, "G")
print(pat1)
doctor = Doctor("fhj", "fjsk", {
    datetime.datetime(2023, 2, 5, 15, 20): pat1
})
doctor.register_patient(pat1, datetime.datetime(2023, 2, 5, 15, 50))
doctor.register_patient(pat2, datetime.datetime(2023, 2, 5, 15, 25))
doctor.register_patient(pat2, datetime.datetime(2023, 2, 5, 15, 50))


prod1 = Product(2500, 1234, 15)
prod2 = Product(1000, 2345, 20)

prod1.buy(13)
prod2.buy(22)
print(prod1)
inv = Inventory([prod1, prod2])
print(inv.sum_of_products())
print(inv.get_by_id(2345))


def book():
    pass1 = Passanger("fdgh", "NewYork", {"penthouse": 1, "single": 3, "double": 2})
    pass2 = Passanger("fff", "NewYork", {"single": 1})
    pass3 = Passanger("fdgh", "NewYork", {"penthouse": 1, "single": 3, "double": 0})
    hotel = Hotel("NewYork", 2, 5, 0)
    print(hotel.free_rooms_list("single"))
    hotel.reserve_roomss(pass2)
    print(hotel)
    hotel.reserve_roomss(pass1)
    print(hotel)
    hotel.reserve_roomss(pass3)
    print(hotel)


book()
