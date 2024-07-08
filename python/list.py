
l = ["Prajwal","Lambda",34,90,2.4,False]

print(l)

l2 = list()
print(l2)

print(l[0])
print(l[::-1])
print(l[0:3])

for i in l:
    print(i,end=',')
print()

if 34 in l:
    print("Yes")
else:
    print("No")


if True in l:
    print("Yes")
else:
    print("No")

print(len(l))

l.append("Lemon")
print(l)
l.insert(1,"Bottle")
print(l)
print(l.pop())
print(l)

l.remove(90)
print(l)

# l.clear()
l.reverse()
print(l)

l2 = [100,34,56,88,32,5,9,10,6,3]
l2.sort()
print(l2)

new_list = sorted(l2)
print(new_list)

my_list = [0]*5
print(my_list)

my_list1 = [2,3,5,6,7]
print(my_list + my_list1)
print(my_list1[::1])
print(my_list1[::2])

l_org = ["TCS","Google","Microsoft","Facebook"]

l_cpy = l_org.copy()
l_cpy.append("Atlassian")
print(l_cpy)
print(l_org)

list = [3,4,6,7,90,180]
list2 = [i*i for i in list]
print(list2)
