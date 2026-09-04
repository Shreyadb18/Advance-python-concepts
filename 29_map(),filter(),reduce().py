#map(), filter(), and reduce() in Python

# map() function

#Example 1: Squaring numbers

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

result = map(square, numbers)
print(list(result))  # [1, 4, 9, 16, 25]

#Example 2: Using lambda with map

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))  # [2, 4, 6, 8, 10]

#Example 3: Multiple iterables

a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))  # [5, 7, 9]

# filter() function

#Example 1: Even numbers

numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)
print(list(result))  # [2, 4, 6]

#Example 2: Using lambda

numbers = [10, 25, 30, 47, 50]
result = filter(lambda x: x > 25, numbers)
print(list(result))  # [30, 47, 50]

# reduce() function

#Example 1: Sum of numbers

from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

result = reduce(add, numbers)
print(result)  # 15

#Example 2: Product of numbers

from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # 120

#Example 3: Maximum value

from functools import reduce

numbers = [10, 20, 5, 8, 100, 3]

result = reduce(lambda a, b: a if a > b else b, numbers)
print(result)  # 100


#Practical Example: Processing Student Scores

from functools import reduce

scores = [45, 67, 89, 34, 76, 90]

# 1. Increase all scores by 5 using map
updated = list(map(lambda x: x + 5, scores))

# 2. Filter only passing students (>= 50)
passed = list(filter(lambda x: x >= 50, updated))

# 3. Find the total marks of all passed students using reduce
total = reduce(lambda x, y: x + y, passed)

print("Updated Scores:", updated)
print("Passed Students:", passed)
print("Total Marks:", total)