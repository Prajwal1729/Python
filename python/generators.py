# A Generator in Python is a function that returns an iterator using the Yield keyword. 
# A generator function in Python is defined like a normal function, but whenever it needs to generate a value,
#  it does so with the Yield keyword ather than return. If the body of a def contains yield, 
# the function automatically becomes a Python generator function. 
# Genenartor function is very efficent whrn we works with large data it's saves a lot of memory.

import sys
def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()
# print(g)

# using loops: it is better
# for i in g:
#     print(i)

# val = next(g)
# print(val)

# val = next(g)
# print(val)

# print(sum(g))

print(sorted(g))

def countDown(num):
    print("Starting")
    while num > 0:
        yield num
        num-=1

cd = countDown(6)

# quite annoying:
# val = next(cd)
# print(val)
# print(next(cd))

for i in cd:
    print(i,end=" ")
print()

# Normal Function
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num+=1
    return nums

mylist = firstn(10)
print(mylist)
print(sum(mylist))
print(sys.getsizeof(firstn(10)))

# generator function

def first_generator(n):
    num = 0
    while num < n:
        yield num
        num+=1

# gg = first_generator(20)
# print(list(gg))

print(list(first_generator(20)))
print(sum(first_generator(20)))
print(sys.getsizeof(first_generator(20)))


def fibo(limit):
    a = 0
    b = 1

    while a < limit:
        yield a
        a,b = b,a+b


fib = fibo(10)
for i in fib:
    print(i,end=" ")
print()

# syntax:
my_gen = (i for i in range(10) if i%2==0)
print(list(my_gen))
for i in my_gen:
    print(i,end=" ")
print()
print(sys.getsizeof(my_gen))

