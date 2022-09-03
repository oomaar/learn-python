class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"name is {self.name} and age is {self.age}"

class Man(Person):
    gender = 'Male'
    no_of_men = 0

    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_men +=1

    def display(self):
        string = super().display()
        return string + f" and voice is {self.voice} and gender is {self.gender}"

class Woman(Person):
    gender = 'Female'
    no_of_women = 0

    def __init__(self, name, age, hair):
        super().__init__(name, age)
        self.hair = hair
        Woman.no_of_women += 1

    def display(self):
        string = super().display()
        return string + f" and hair is {self.hair} and gender is {self.gender}"

man = Man("Islam", 30, "hard")
print(man.display())
print(Man.no_of_men)

woman = Woman("Esraa", 30, "long")
print(woman.display())
print(woman.no_of_women)

woman = Woman("Dalia", 20, "long")
print(woman.display())
print(woman.no_of_women)