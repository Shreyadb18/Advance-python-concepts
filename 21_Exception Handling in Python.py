#Exception Handling in Python

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")

finally:
    print("Program completed")

# Handling Invalid Input

try:
    age = int(input("Enter your age: "))
    print("Your age is", age)

except ValueError:
    print("Please enter a valid number")

#Using else

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result =", result)

#Handling List Index Error

try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Index does not exist")

#Handling Dictionary Key Error

try:
    student = {
        "name": "Shreya",
        "age": 20
    }

    print(student["marks"])

except KeyError:
    print("Key does not exist")

#Handling File Error

try:
    file = open("student.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

#using raise to raise an exception

age = int(input("Enter your age: "))

if age < 18:
    raise Exception("You are not eligible")

print("You are eligible")