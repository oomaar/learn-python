class Student:
    no_of_students = 0

    def __init__(self, name, age=0, courses=[]):
        self.name = name
        self.age = age
        self.courses = courses
        Student.no_of_students += 1

    def describe (self):
        print(f"my name is {self.name} and my age is {self.age}")

    def is_old(self, num):
        if self.age <= num:
            print("Student is not old")
        else:
            print("student is old")

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

student1 = Student("Omar", 28, ['CS', 'Math'])

print(student1.get_name())
student1.set_name("Islam")
print(student1.get_name())