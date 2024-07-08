# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def walk(self):
#         print("The lion walk")


# a1 = Animal("Lion")
# print(a1.walk())


class Student:

   college_name = "VJTI"
   name = "anonymous"    # class attribute
   # default constructor
   # def __init__(self):             # type: ignore
    #     pass
    
   # parameterized constructor
   def __init__(self,fullname,marks):
        self.name = fullname    # object attribute(more prefferred) > class attribute
        self.marks = marks
        print("Adding the student in the database")

   def hello(self):
       print("welcome to the new students")

   def get_marks(self):
       return self.marks
       

s1 = Student("Prajwal",72)
print(s1.name,s1.marks)

s2 = Student("Karan",67)
print(s2.name,s2.marks)

print(s2.college_name)
print(Student.college_name)
print(s1.name)
print(s1.get_marks())
print(s1.hello())


class Student1:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def print_average(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print(f"Hello,{self.name} your avg score is:",sum/3)
    

s = Student1("Prajwal",[89,90,95])
print(s.print_average())



# static methods are the methods which dont't use self parameter
# @staticmethod: It converts the normal function to the static method, this is called as decorator.







