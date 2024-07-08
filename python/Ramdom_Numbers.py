import random

# a = random.random()
# print(a)

# b = random.uniform(1,10)
# print(b)

# c = random.randint(1,100)
# print(c)

# # similar method
# d = random.randrange(2,10)
# print(d)


# x = random.normalvariate(0,1)
# print(x)

ls = list("ABCDEFGHI")
# print(ls)

# y = random.choice(ls)
# print(y)

# m = random.sample(ls,3)
# print(m)

# l = random.choices(ls,k=3)
# print(l)

# random.shuffle(ls)
# print(ls)

random.seed(1)
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,100))

random.seed(2)
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,100))

random.seed(1)
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,100))

random.seed(2)
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,100))

import secrets

a = secrets.randbelow(10)   # it will not include 10
print(a)

b = secrets.randbits(4)
print(b)

list1 = secrets.choice(ls)
print(list1)

import numpy as np

a = np.random.rand(3,3)
print(a)

b = np.random.randint(0,10,3)
print(b)

c = np.random.randint(0,10,(3,4))
print(c)


arr = np.array([[1,2,3],[4,5,6],[9,10,11]])
print(arr)

np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))

np.random.seed(1)  
print(np.random.rand(3,3))
