# A Generator in Python is a function that returns an iterator using the Yield keyword.
# In Python, a generator is a function or expression that will process a given iterable one object 
# at a time, on demand.
# This is Python Generator function
# def fib(limit):
#     a,b = 0,1

#     while a < limit:
#         yield a
#         a,b = b,a+b


# for i in fib(8):
#     print(i,end=" ")


# def factorial_generator(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
#         yield fact
        
# n = 8
# for res in factorial_generator(n):
#     print(res)


# data types: int,float,string,boolean
# user input

# x = int(input("Enter a Number:"))
# print(x)

print(4.5,"Hello world")

a = 78
print(f"The value of number is {a}")

# Arthematic Operators:

# x = 67
# y = 45
# print(x+y)
# print(x-y)
# print(x%y)
# print(x//y)
# print(x*y)
# print(x**y)

# a = int(input("Enter a Number: "))
# print(a-9)
# print(float(a)-10)


# String Methods:

a = "The man who knew the Infinity"
print(a.upper())
print(a.lower())

print(a[::-1])
b = "hello"
print(b.capitalize())
print(a.count("i"))
print(a.count("I"))
print(a.lower().count("i"))

x = 3
y = "Prajwal"
z = "Inteligent"
print(x*y)
print(y+z)

# Conditional Operators:

x = "Hello"
y = "hello"
print(x!=y)
print(x>y)
print(x<y)

print('a' > 'Z')
print(ord("a"))   # to print the ASCII CODE
print(ord('~'))
print(ord('z'))
print('a'>'z')

x = 6
y = 56
z = 90

res1 = x == y
res2 = y > x
res3 = z < x + 2

res4 = res1 or not res2 or res3
print(res4)

print(not False)
print(not True)

x = "Prajwal"

if x == "Prajwal":
    print("You are good enough at python")

elif x == "Elon Musk":
    print("You are Intelligent in Python")
else:
    print("You want to learn python")


animal = "Eagle"


# Switch Case Statement:
match animal:
    case "Eagle" | "Bird":
        print("Bird")
    case "Lion" | "Tiger":
        print("Mammal")
    case "Python" | "Crocodile":
        print("Reptile") 
    case _:
        print("Unknown Class")


# list: It is mutuable
x = ["Prajwal",True,2.3,23,"Infinity"]
print(x)
print(type(x))
print(len(x))

x.append("Hello")
print(x)
x.extend([34,90,12,3,19,100])
print(x)
print(x.pop())
print(x.pop(3))
y = x[:]
print(y)

# tuple: it is immutable

x = (45,89,100,103)
print(x)
print(type(x))

y = [(100,200,"Infinity"),[34,90,100],12,3,78,16]
print(y)

# loops:
n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,10):
    print(i,end=" ")
print()

for i in range(10,-1,-2):
    print(i,end=" ")
print()

for i in range(len(y)):
    print(y[i],end=" ")
print()

# enumerate: enumerate(iterable,start)
# The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object.
x = ["Prajwal",45,2.97,True]
for i in enumerate(x):
    print(i,end=" ")
print()

for i,element in enumerate(x):
    print(i,element)

i = 0
while i<10:
    print(i,end=" ")
    i+=1

# while True:
#     print("Run")
#     i+=1
#     while True:
#         if i == 10:
#             break
print()

# slicing:

x = [23,"Harvey",6.67,True,"Spectre"]
print(x[::-1])
print(x[:-1])
print(x[0:3])
print(x[0:])
print(x[0:4])

# set:
X =  set()
s = {34,90,100,100}
print(s)
print(type(s))
s.add(45)
print(s)
s.remove(34)
print(s)
print(100 in s)
print(34 in s)

s1 = {"Prajwal",18,4,2001}
s2 = {"Harvey",67,True,2.3}
print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))

# dictionaries:

x = {"name": "Prajwal","marks": 71,"role":"Developer","marks":89}
print(x)
print(type(x))
print(x.values())
print(x.keys())
print(list(x.values()))
print(list(x.keys()))

for key,value in x.items():
    print(key,value)

# List Comprehensions:
x = [x*i for x in range(10)]
print(x)

x = [i for i in range(100) if i%2==0]
print(x)

# use tuple ----> returns the garbage value
y = (i for i in range(40) if i%2==0)
print(y)


# functions:
def func(x,y):
    print("Run",x,y)
    return x*y,x/y

f1,f2 = func(90,23)
print(f1,f2)

# unpack operator: *args and **KWARGS, unpack operator seprates all the elemnts in the list into the
# individual elements.
# "*" use in list or tuple and "**" is use in dictonaries.
def func1(x):
    def func2():
        print(x)
    return func2

x = func1(300)
x()

def func3(x,y):
    print(x,y)
func3(**{"x":100,"y":300})

pairs = [(23,90),(3,5)]
for pair in pairs:
    func3(*pair)
x = [12,3,4,445555,90]
print(*x)

def func4(*args,**kwargs):
    print(args,kwargs)

func4(1,2,3,45,one=90,two=100)


# SCOPE: Local and Global:
x = "Prajwal"

def func5(name):
    global x
    x = name

print(x)
func5("changed")
print(x)
 

# try and except block and exception

# raise Exception("Bad")
# raise FileExistsError("")

# Handling Exceptions:
try:
     x = 100/0
except Exception as e:
    print(e)
finally:
    print("finally")

# lambda: one line anonymous function
x = lambda x : x*10
print(x(5))

x = lambda x,y: x+y
print(x(45,90))

# map and filter function:

x = [34,90,12,3,4,78,100]
mp = map(lambda i: i*2,x)
print(list(mp))


y = [9,45,12,2,3,67,90]
f = filter(lambda i:i%2==0,y)
print(list(f))

# f strings:
x = f"hello {6+90}"
print(x)

x = 1
y = 0
z = 8
print(f"The values {x} means unity,{y} means empty and {z} means infinity")














