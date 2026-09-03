#Decorators

# Functions are First-Class Citizens in Python

def welcome(func):
    def wrapper():
        print("Namaskara!")
        func()
        print("Take care!")
    return wrapper

@welcome
def intro():
    print("I am Shreya from Karnataka.")

intro()

#Decorator with Arguments

def greet(func):
    def wrapper(name):
        print("Hello!")
        func(name)
        print("Have a nice day!")
    return wrapper

@greet
def say_name(name):
    print(f"My name is {name}")

say_name("Shreya")

#Decorator for Logging

def logger(func):
    def wrapper():
        print(f"Function '{func.__name__}' is being called.")
        func()
    return wrapper

@logger
def greet():
    print("Hey there!")

greet()

#example:

def login_required(func):
    def wrapper():
        print("Checking if user is logged in...")
        func()
    return wrapper

@login_required
def view_profile():
    print("Ravi's profile opened.")

view_profile()