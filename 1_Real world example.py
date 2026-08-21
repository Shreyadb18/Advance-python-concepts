'''1. Banking System Simulation

Design a system to simulate a bank's operations, where users can create accounts, deposit and withdraw money, and check their account balance.

Extend functionality to include multiple account types (e.g., savings, current) with unique behaviors like interest calculation or overdraft limits.
Emphasize encapsulation, inheritance and polymorphism.'''

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings account withdrawal successful")
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance + 5000:
            self.balance -= amount
            print("Current account withdrawal successful")
        else:
            print("Overdraft limit exceeded")


# Savings Account
print("----- Savings Account -----")

s1 = SavingsAccount("Shreya", 10000)

s1.show_balance()
s1.deposit(2000)
s1.withdraw(5000)
s1.show_balance()


# Current Account
print("\n----- Current Account -----")

c1 = CurrentAccount("Rahul", 5000)

c1.show_balance()
c1.deposit(2000)
c1.withdraw(10000)
c1.show_balance()