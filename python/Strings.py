# Strings are immutale they can't be changed when assigned
my_str = "The man who knew the infinity"
print(my_str)

char = my_str[0]
print(char)
print(my_str.lower())

print(my_str[1:5])
print(my_str[::1])
print(my_str[::2])
print(my_str[::-1])

s1 = "Black"
s2 = "Hole"
print(s1 + s2)

for i in s2:
    print(i,end=" ")

print()
if i in my_str:
    print("YES")
else:
    print("No")


s3 = "         hello       "
print(s3.strip())
print(my_str.upper())
print(my_str.lower())
print(my_str.startswith("the"))
print(my_str.endswith("infinity"))
print(my_str.find("o"))
print(my_str.count("in"))
print(s1.replace('Black','univserse'))

my_list = my_str.split()
print(my_list)
print(' '.join(my_list))

from timeit import default_timer as timer 

my_list = ["P"]*6
print(my_list)

start = timer()
my_str = ""

for i in my_list:
    my_str+=i
stop = timer()
print(stop-start)
print(my_str)

start = timer()
print(' '.join(my_list))
stop = timer()
print(stop-start)


# v = "Mike"
# my_str = "The variable is %s" % v
# print(my_str)

b = 4
s = "The variable is %d" % b
print(s)

c = 4.58994
n = "The variable is %f" % c
print(n)

print(f"The statement is {my_str}")





