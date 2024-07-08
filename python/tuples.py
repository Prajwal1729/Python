tup = (2,3,4,"Prajwal",3.4,True)

print(tup)
print(tup[0:3])
# tup.append(8)    ----> It will throw error because it is tuple immutable.
print(tup)

print(tup[::-1])
# print(tup.pop())    ----> It will throw error because it is tuple immutable.

tup1 = (56,100,[45,90,34,100])
print(tup1[0:])

tup2 = tuple(["IT","CORE","sales & markerting","SCM","CRM"])
print(tup2)
print(tup2[3])

for l in tup:
    print(l,end=" ")
print()

if True in tup:
    print("Yes")
else:
    print("No")

print(len(tup2))

tup3 = ('b','a','n','a','n','a')
print(tup3.count('a'))

print(tup3.index('n'))

l = list(tup2)
print(l)
print(type(l))

t = tuple(tup3)
print(t)
print(type(t))
print(tup2[1:3])
print(tup1[::1])

print(tup1[::2])

my_tup = "Max","Boston",34
name,city,age= my_tup
print(name)
print(age)
print(city)

my_tup1 = (0,1,2,3,4,5)

i1,*i2,i3 = my_tup1
print(i1)
print(i2)
print(i3)

# tuple is more efficent whrn working with large data
import sys
my_list = [0,1,2,4,"Hello",True]
my_tuple = (0,1,2,4,"Hello",True)

print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")

print(my_tuple.index(4))  # ---> it will return the index inside the tuple
print(my_tuple.index("Hello"))


import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=100000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=100000))






