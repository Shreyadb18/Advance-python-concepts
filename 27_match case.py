#match case

#Example1:

day = "Sunday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("Just another weekday.")

#Example2:


a = 10
b = 5
operator = "+"

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")

#Example3:

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Add")
    case 2:
        print("Subtract")
    case 3:
        print("Multiply")
    case 4:
        print("Divide")
    case _:
        print("Invalid choice")
