class Person:
    def __init__(self, namem, ageg, gendere):
        self.name = namem
        self.age = ageg
        self.gender = gendere
    def introduce(self):
        print(f"Hi there my name is {self.name}, and I am {self.age} and my gender is {self.age}")

person_object = Person("John Doe", 76, "male")
person_object.introduce()