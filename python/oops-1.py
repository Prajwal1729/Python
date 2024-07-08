# Abstraction:
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car is started....")


# c1 = Car()
# c1.start()

# Question:
# class Account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.acount_no = account_no
    
#     def debit(self,amount):
#         self.balance-=amount
#         print("Your debit is",amount)
#         print("total balance is:",self.print_balance())
    
#     def credit(self,amount):
#         self.balance+=amount
#         print("Your credit is",amount)
#         print("Your balance is:",self.print_balance())

#     def print_balance(self):
#         return self.balance


# a = Account(10000,40238299992)
# a.debit(1000)
# a.credit(500)
# a.print_balance()


# del keyword is use to delete the object properties or objects 

# class Student:
#     def __init__(self,name):
#         self.name = name


# s1 = Student("Mike")
# print(s1.name)
# del s1.name
# print(s1.name)

# private attributes:

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass      # this has private now(with two __), 
                                        # we cannot access outside the class
    
    def reset_pass(self):
        print(self.__acc_pass)

    def __hello(self):
        print("Hello, welcome to our bank")
    
    def welcome(self):
        self.__hello()


a1 = Account(90667727,"Coder@18")
print(a1.acc_no)
# print(a1.__acc_pass)
# print(a1.__hello)
print(a1.welcome())

# Inheritance:

# class Car:
#     @staticmethod
#     def start():
#         print("Car Started....")

#     @staticmethod
#     def stop():
#         print("Car Stopped...")
    
# class Lamborghini(Car):
#     def __init__(self,name):
#         self.name = name


# c1 = Lamborghini("Aventodor")
# c2 = Lamborghini("Cyan")

# print(c1.start())
# print(c2.stop())


# Mulitlevel Inheritance:
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started....")

    @staticmethod
    def stop():
        print("Car Stopped...")
    
class Lamborghini(Car):
    def __init__(self,name,type):
        super().__init__(type)       # here super key use access the attributes and methods of parent class
        self.name = name
        super().start()
        super().stop()


c1 = Lamborghini("cyan","electric")
print(c1.name)
print(c1.type)


# class Aventodor(Lamborghini):
#     def __init__(self,type):
#         self.type = type

# c1 = Aventodor("electric")
# print(c1.start())


# Multiple Inhertance:
class A:
    a = "Welcome to class A"

class B:
    b = "Welcome to class B"

class C(A,B):
    c = "Welcome to class C"


c1 = C()

print(c1.a)
print(c1.b)


# class Person:
#     name = "anonoymous"

#     @classmethod                   # it can access or modify class state & generally for utility.  
#     def changename(cls,name):
#         cls.name = name


# P1 = Person()
# print(P1.changename("Prajwal"))


class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    # def calculate_percentage(self):
    #       self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

# we use @property decorator on any method inside the class to use the method inside the property.

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


s = Student(90,80,98)
print(s.percentage)

s.chem = 93
print(s.percentage)


# polymorphism: Operator overloading
# When the same operator is allowed to have diffrent meaning according to the context.

# for eaxmple:

print([1,4,5] + [6,9,3])

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    
    def show_num(self):
        print(self.r,"i", "+", self.i,"j")

    def __add__(self,num2):       # So this is the dunder function
        new_real = self.r + num2.r
        new_img = self.i + num2.i   
        return  Complex(new_real,new_img)
    
    def __sub__(self,num2):
        new_real = self.r - num2.r
        new_img = self.i - num2.i
        return Complex(new_real,new_img)
        

c1 = Complex(2,9)
c2 = Complex(9,4)
c1.show_num()
c2.show_num()

c3 = c1+c2
c3.show_num()

c4 = c1 - c2
c4.show_num()

import math
class Circle:
    def __init__(self,r):
        self.r = r

    def Area(self):
        return math.pi*self.r*self.r
    
    def perimeter(self):
        return 2*math.pi*self.r
    
c1 = Circle(34)
print(c1.Area())
print(c1.perimeter())


class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(f"The role is {self.role},department is {self.dept} and salary is {self.salary}")

    
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","90000")



e1 = Employee("Developer","Production",60000)
e1.show_details()

e2 = Engineer("Elon Musk",40)
e2.show_details()



class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price


odr1 = Order("choclates",1200)
odr2 = Order("Cell",120)

print(odr1 > odr2)

