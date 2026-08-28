#File Handling in Python

#opening a file

file = open("student.txt", "r")
content=file.read()
print(content)
file.close()

#reading from a file

#1. read() – Reads entire file

file = open("notes.txt", "r")
print(file.read())
file.close()

#2. readline() – Reads one line

file = open("notes.txt", "r")
print(file.readline())
file.close()

#3. readlines() – Reads all lines into a list

file = open("notes.txt", "r")
lines = file.readlines()
print(lines)
file.close()

#Writing to a file

file = open("data.txt", "w")
file.write("Namaskara Bengaluru!\n")
file.write("Python is awesome!")
file.close()

#Appending to a File

file = open("data.txt", "a")
file.write("\nThis line is added later.")
file.close()

#Using with Statement

with open("students.txt", "r") as file:
    content = file.read()
    print(content)

#Writing List of Data to File

students = ["Ravi", "Meena", "Dinesh"]
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

#Reading File and Processing Each Line

with open("students.txt", "r") as file:
    for line in file:
        print("Student:", line.strip())