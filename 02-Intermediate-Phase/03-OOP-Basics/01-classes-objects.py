# Object-Oriented Programming Basics
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Create objects
person1 = Person("Alice", 25)
print(person1.introduce())

# TODO: Practice inheritance, encapsulation
