#SOLID Principles in Python

#1. Single Responsibility Principle (SRP)
#Definition: A class should have only one reason to change. That means, a class should do only one job.

class Student:
    def __init__(self, name):
        self.name = name

class StudentDatabase:
    def save(self, student):
        print(f"Saving {student.name} to database...")

class ReportCard:
    def generate(self, student):
        print(f"Generating report card for {student.name}...")

#2. Open/Closed Principle (OCP)
#Definition: Software entities (classes, functions, etc.) should be open for extension but closed for modification.

class Discount:
    def get_discount(self):
        return 0

class RegularCustomer(Discount):
    def get_discount(self):
        return 10

class PremiumCustomer(Discount):
    def get_discount(self):
        return 20

#3. Liskov Substitution Principle (LSP)
#Definition: Subclasses should be able to replace their parent class without breaking the program.

class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying...")

class Penguin(Bird):
    def move(self):
        print("Swimming...")

#4. Interface Segregation Principle (ISP)
# Definition: Don’t force a class to implement methods it does not use.

class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")

#5. Dependency Inversion Principle (DIP)
#Definition: High-level modules should not depend on low-level modules. Both should depend on abstractions.

class InputDevice:
    def input(self):
        pass

class Keyboard(InputDevice):
    def input(self):
        return "User typing..."

class Mouse(InputDevice):
    def input(self):
        return "Mouse clicked"

class Computer:
    def __init__(self, device: InputDevice):
        self.device = device

    def get_input(self):
        return self.device.input()