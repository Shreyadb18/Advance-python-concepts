#Iterators and Generators in Python

numbers = [1, 2, 3]

# Get iterator from list
it = iter(numbers)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # Raises StopIteration

#Using Iterators with Loops

for num in [1, 2, 3]:
    print(num)

#Creating Your Own Iterator

class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        num = self.start
        self.start -= 1
        return num

cd = CountDown(5)

for i in cd:
    print(i)

#Generators in Python
    

def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

#Generators with Loops

def squares(n):
    for i in range(n):
        yield i * i

for val in squares(5):
    print(val)

#Generator Expressions

gen_exp = (x*x for x in range(5))
print(next(gen_exp))  # 0
print(next(gen_exp))  # 1
print(list(gen_exp))  # [4, 9, 16]


#Real-Life Use Cases

def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_numbers()
for i in range(5):
    print(next(gen))

    