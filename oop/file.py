from datetime import date

class Student:
    no_of_students = 0

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        Student.no_of_students += 1

    def describe (self):
        print(f"my name is {self.name} and my age is {self.age}")

    @classmethod
    def initFromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def veg(cls):
        return cls(['Mushrooms', 'onions', 'olives'])

    @classmethod
    def margrita(cls):
        return cls(['Motzarella', 'sause'])


pizza1 = Pizza(['Tomatto', 'Olives'])
pizza2 = Pizza.veg()
pizza3 = Pizza.margrita()

print(pizza1)
print(pizza2)
print(pizza3)