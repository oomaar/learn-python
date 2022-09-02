class Student:
    no_of_students = 0

    def __init__(self, name, age=0, courses=[]):
        self.name = name
        self.age = age
        self.courses = courses
        Student.no_of_students += 1

student1 = Student("Omar", 28, ['CS', 'Math'])
student2 = Student("Menna")
student2.age = 27
student2.courses = ['CS', 'Math']

print(student1.age, student2.age, student2.name)
print(Student.no_of_students)