arg = 5

cpy = arg
print(cpy)

org = [1,2,3,4,5]
# cpy = 6
cpy = org
cpy[0] = -10
# print(cpy)
# print(org)

# shallow copy: one level deep,only references of nested child objects.
# deep copy: full independent copy.   

import copy
org = [[0,1,2,3,4],[6,7,8,10,11,12]]
cpy = copy.copy(org)
# cpy = org.copy()
# cpy = list(org)
# cpy = org[:].copy()
cpy1 = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)
print(cpy1)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Company:
    def __init__(self,boss,emp):
        self.boss = boss
        self.emp = emp


p1 = Person("Harvey",34)
p2 = Person("Mike",28)
# p2 = copy.copy(p1)

print(p1.age)
print(p2.age)

c1 = Company(p1,p2)
c2 = copy.deepcopy(c1)
c2.boss.age = 45
print(c2.boss.age)
print(c1.boss.age)





