#Constructors and self keyword

#1.the __init__() constructors

class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

#2.using self in class methods

class Person:
    def __init__(self, name, age):
        self.name = name  # 'self.name' is an instance variable
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Arjun", 22)
person1.introduce()

#3.creating multiple objects with different attributes

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: ₹{self.price}")

laptop1 = Laptop("Dell", 45000)
laptop2 = Laptop("HP", 55000)

laptop1.show_info()
laptop2.show_info()

#4.optional parameters in constructor
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Python Programming")
book2 = Book("Machine Learning", "Andrew Ng")

book1.show_book()
book2.show_book()


# 1. Class with Constructor

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def display(self):
        print("Movie Title:", self.title)
        print("Rating:", self.rating)


# Create a Movie object
movie1 = Movie("Inception", 8.8)

# Display movie details
movie1.display()


print("\n----------------------\n")


# 2. Class with Default Parameters

class Employee:
    def __init__(self, name, designation, salary=30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


# Create Employee objects
emp1 = Employee("Alice", "Manager", 50000)
emp2 = Employee("Bob", "Developer")
emp3 = Employee("Charlie", "Designer", 45000)
emp4 = Employee("David", "Intern")

# Display employee details
emp1.display()
print()

emp2.display()   # Uses default salary
print()

emp3.display()
print()

emp4.display()   # Uses default salary