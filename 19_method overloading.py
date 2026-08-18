#method overloading

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c  # Handles both 2 and 3 parameter cases

# Usage
math = MathOperations()
print(math.add(5, 10))     # Two arguments
print(math.add(5, 10, 15)) # Three arguments

#method overriding

class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")  # Overrides the parent class method

# Usage
animal = Animal()
animal.sound()
dog = Dog()
dog.sound()  # Calls the overridden method in Dog class

#super() function

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the parent class's __init__ method
        self.breed = breed

    def sound(self):
        super().sound()  # Calling the parent class's sound method
        print(f"{self.name} barks")

# Usage
dog = Dog("Buddy", "Labrador")
dog.sound()

#Abstract classes and methods

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method with no implementation

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

# Usage
car = Car()
car.start_engine()