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

student1 = Student("Omar", 28, ['CS', 'Math'])
student2 = Student("Menna", 27, ['CS', 'Math'])

student1.describe()
student2.describe()

student1.is_old(50)