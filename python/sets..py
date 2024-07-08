s = {34,1,2,3,4,510}
print(s)

my_set = set([6,5,3,1])
print(my_set)

my_set1 = set(['h','e','l','l','o'])
print(my_set1)
print(type(my_set))

my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(5)
my_set.add(6)
print(my_set)
my_set.remove(3)

my_set.discard(4)
print(my_set)
print(my_set.pop())
# print(my_set.clear())

for i in my_set:
    print(i,end=" ")

print()
if 1 in my_set:
    print("Yes")
else:
    print("No")


s1 = {1,3,5,7,9}
s2 = {8,10,4,6,2,0}
s3 = {2,3,5,7}

u = s1.union(s2)
print(u)
i = s1.intersection(s3)
print(i)

j = s1.intersection(s2)
print(j)

a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,10,11,12}

diff = a.difference(b)
print(diff)

diff1 = b.symmetric_difference(a)
print(diff1)

a.update(b)
print(a)

a.intersection_update(b)
print(a)

a.difference_update(b)
print(a)

a.symmetric_difference_update(b)
print(a)

print(a.issubset(b))

print(a.issuperset(b))
print(b.issuperset(a))

print(a.isdisjoint(b))

a = b
b.add(7)
print(b)
print(a)

a = frozenset([2,3,4,5,6])
# a.remove(1)    -----> it will throw an error
print(a)





