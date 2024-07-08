#itertools: product,permuations,combinations,accumalate,groupby and infinite iterators

from itertools import product
a = [1,2]
b = [3]

prod = product(a,b,repeat=2)
print(list(prod))

from itertools import permutations
x = [1,2,3]
perm = permutations(x,2)
print(list(perm))

from itertools import combinations,combinations_with_replacement
y = [1,2,3,4]
comb = combinations(y,2)
comb1 = combinations_with_replacement(y,2)
print(list(comb))
print(list(comb1))

from itertools import accumulate
import operator
p = [1,2,3,4]
accum = accumulate(p,func=operator.mul)
print(list(accum))

from itertools import groupby
# def smaller_than_3(x):
#     return x<3
# l = [1,2,3,4]

# g_obj = groupby(l,key=lambda x:x<3)
# print(list(g_obj))

# for key,value in g_obj:
#     print(key,list(value))

a = [1,2,3]
from itertools import count,cycle,repeat
for i in count(10):
    print(i)
    if i == 15:
        break
for i in cycle(a):
    print(i)

for i in repeat(1,4):
    print(i)


persons = [{'name':'Prajwal','age':23},{'name':'Dan','age':30},
           {'name':'Mike','age':28},{'name':'Harvey','age':30}]

g_obj = groupby(persons,key=lambda x: x['age'])
for key,value in g_obj:
    print(key,list(value))




