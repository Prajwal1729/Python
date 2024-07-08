def print_num(n):
    print(n)

print_num(23)

def foo(a,b,c):
    print(a,b,c)

foo(a=1,b=2,c=3)

def print_val(a,b,*args,**kwargs):
    print(a,b)

    for arg in args:
        print(arg)
    for k in kwargs:
        print(k,kwargs[k],end=" ")

print_val(1,2,3,4,5,6,7,x=90,y=100)
print()

def foo1(a,b,*,c,d):
    print(a,b,c,d)

foo1(1,2,c=3,d=4)

def foo2(*args,last):
    for a in args:
        print(a)
    print(last)

foo2(1,2,3,last=100)

def foo3(a,b,c):
    print(a,b,c)

ls = [12,4,5]
tup = (23,90,100)
foo3(*ls)
foo3(*tup)

mydict = {'a': 1,'b':2,'c':3,}
foo3(**mydict)


def foo4(ls):
    ls = [200,900,1000]
    ls.append(4)
    ls[0] = -100

list1 = [1,3,4]
foo4(list1)
print(list1)
# print(list1)

def foo5(a,b,*args,**kwargs):
    print(a)
    for arg in args:
        print(arg,end=" ")
    for key in kwargs:
        print(key,":",kwargs[key])

foo5(1,2,3,4,5,6,x=100,y=200)

# def foo6(a,b,*,c):
#     print(a,b,c)

# foo6(1,3,c=90)

def foo6(a,b,c):
    print(a,b,c)
my_tup = (3,9,10)
foo6(*my_tup)

my_dict = {'a':1,'b':2,'c':3}
foo6(**my_dict)

nums = [1,2,3,4,5,6,7,8]

*s,e = nums
print(s)
print(e)

s,*e = nums
print(s)
print(e)

s,*m,e = nums
print(s)
print(m)
print(e)

my_list = [1,2,3]
my_tup = (4,5,6)

new_list = [*my_list,*my_tup]
print(new_list)


a = {'a':1,'b':3}
b = {'c':90,'d':100}

new_dict = {**a,**b}
print(new_dict)