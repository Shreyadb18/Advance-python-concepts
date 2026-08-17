#Getters, Setters

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Invalid age")

# Usage
student = Student("Anita", 20)
print("Age:", student.get_age())  # Accessing age with getter
student.set_age(21)  # Modifying age with setter
print("Updated Age:", student.get_age())

#example 2

class Employee:
    def __init__(self):
        self.__salary = 0

    # Setter
    def set_salary(self, salary):
        self.__salary = salary

    # Getter
    def get_salary(self):
        return self.__salary


e = Employee()

e.set_salary(25000)

print("Salary:", e.get_salary())

#example3: Age example

class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative")

    def get_age(self):
        return self.__age


p = Person()

p.set_age(20)

print("Age:", p.get_age())

#example4: using @property

class Student:
    def __init__(self):
        self.__name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


s = Student()

s.name = "Shreya"       # Setter
print(s.name)           # Getter

#Real life example:Bank account

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount()

account.set_balance(5000)

print("Balance:", account.get_balance())