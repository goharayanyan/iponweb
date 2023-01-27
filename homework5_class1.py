class Company:
    def __init__(self, n, f, e):
        self.company_name = n
        self.founded_at = f
        self.employes_count = e

    def __repr__(self):
        return "company-{}, founded at-{}, employes-{}".format(self.company_name, self.founded_at, self.employes_count)


class Job:
    def __init__(self, c, s, e, p):
        self.company = c
        self.salary = s
        self.experience = e
        self.position = p

    def __repr__(self):
        return "comapny-{},salary-{},experience-{},position-{}".format(self.company, self.salary, self.experience, self.position)

    def change_salary(self, change):
        self.salary = change

    def change_experience(self, change):
        self.experience = change

    def change_position(self, change):
        self.position = change


class Person:
    def __init__(self, n, s, g, age, a, f, j):
        self.name = n
        self.surname = s
        self.gender = g
        self.age = age
        self.address = a
        self.friends = f
        self.jobs = j

    def __repr__(self):
        return "name-{},surname-{},gender-{},age-{},address-{},friends-{},job-{}".format(self.name, self. surname, self.gender, self.age, self.address, self.friends, self.jobs)

    def add_friend(self, other):
        self.friends.append(other)
        other.friends.append(self)

    def remove_friend(self, other):
        self.friends.remove(other)

    def add_job(self, job):
        self.jobs.append(job)
        aca.employes_count += 1

    def display_job(self):
        print(self.jobs)


aca = Company("ACA", 2010, 100)
manager = Job("programming", 1000, 1, "junior")
lawer = Job("law", 900, 2, "middle")
person1 = Person("Emmy", "Williams", "Female", 25, "Burbank 35", [], [manager])
person2 = Person("John", "Gates", "Male", 43, "Wolf street", [], [lawer])
print(aca)
print(manager)
manager.change_salary(1500)
print(manager)
print(person1)
print(person2)
person1.add_friend(person2)
person2.remove_friend(person1)
print(person1)
print(person2)
person2.add_job(manager)
print(aca)
person2.display_job()



