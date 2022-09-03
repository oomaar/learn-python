class Student:
    no_of_students = 0

    def __init__(self, name, age=0, courses=[]):
        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.no_of_students += 1

    def describe (self):
        print(f"my name is {self.__name} and my age is {self.__age}")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

student1 = Student("Omar", 28, ['CS', 'Math'])

print(student1.get_name())
print(student1.get_age())
student1.set_name("Omar Hassan")
print(student1.get_name())
student1.set_age(29)
print(student1.get_age())
print(student1.describe())