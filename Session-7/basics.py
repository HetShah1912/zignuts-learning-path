# Lecture 1

# print("Hello World")

# name = "Het"
# age = 21

# age2 = age

# print("My Name is :",name)
# print("My Age is :",age2)

# print(type(name))
# print(type(age))

# # Arithmatic Operators
# a = 5 
# b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)

# # Relational Operators
# a = 50
# b = 20

# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)
# print(a >= b)
# print(a <= b)

# # Assignment Operators
# num = 10

# num += 10
# num -= 10
# num *= 10
# num /= 10
# num %= 10
# num **= 5
# print(num)

# # Logical Operators

# a = 50
# b = 30
# print(not(a > b))
# print(not False)

# val1 = True
# val2 = False

# print(val1 and val2)
# print(val1 or val2)

# # Type Conversions(Implicit)
# a = 2
# b = 4.25
# sum = a+b
# print(sum)

# a = "2"
# print(a+b)

# # Type Casting
# print(int(a)+b)

# # User Input
# name = input("Enter Name : ")
# print(name)

# val = int(input("Enter Value : "))
# print(val, type(val))










# # Lecture 2
# # String Operations

# str1 = "This is string.\nWe are creating it in\t python"
# print(str1)

# # Concatenations
# str1 = "Hello"
# str2 = "World"
# final = str1 + " " + str2
# print(final)

# # length
# str1 = "Hello"
# print(len(str1))

# # indexing : only for access not for modification
# str1 = "Hello"
# print(str1[1])

# # slicing : access part of string
# str1 = "Hello"
# print(str1[1:4])
# print(str1[:4])
# print(str1[1:])

# # negative index
# str1 = "Hello"
# print(str1[-3:-1])

# str = "coder"
# print(str.endswith("er"))
# print(str.capitalize())
# print(str.replace("c","k"))
# print(str.find("q"))
# print(str.count("e")) #occurences

# # Conditionals
# age = 21
# if( age > 18 ):
#   print("Eligible")

# light = "green"
# if(light == "green"):
#   print("Go")
# elif(light == "yellow"):
#   print("Wait")
# elif(light == "red"):
#   print("stop")
# else:
#   print("Invalid Traffic Light")


# marks = int(input("Enter Marks : "))

# if(marks >= 90):
#   print("Grade A")
# elif(marks >= 80 and marks < 90):
#   print("Grade B")
# elif(marks >= 70 and marks < 80):
#   print("Grade C")
# elif(marks >= 60 and marks < 70):
#   print("Grade D")
# else:
#   print("Grade F")


# age = 78

# if(age >= 18):
#   if(age <= 75):
#     print("Can Drive")
#   else: 
#     print("Can't Drive")
# else:
#   print("Can't Drive")










# # Lecture 3

# # List and Tuples
# # Lists
# marks = [39.8, 56.2, 98.7, 45.8]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[1])
# print(marks[0])

# studentInfo = ["Het", 20, 78.5, "Ahmedabad"]
# print(studentInfo)

# # str = "Hello"
# # str[0] = "A" # Strings are immutable

# studentInfo[1] = 21
# print(studentInfo) # Lists are mutable

# # slicing in list
# print(marks[1:4])

# # negative indexing
# print(marks[-4:-1])

# # methods 
# lst = [2, 1, 3]
# print(lst)
# lst.append(4)
# print(lst)
# lst.sort()
# print(lst)
# lst.sort(reverse = True)
# print(lst)
# chars = ['a', 'd', 'c', 'b']
# print(chars)
# chars.sort()
# print(chars)
# lst.reverse()
# print(lst) 
# lst.insert(1, 7) # add element at index (index, element)
# print(lst)
# lst.remove(7) # remove first occurence of element
# print(lst)
# lst.pop(2) # remove element from given index
# print(lst)

# # Tuples
# tup = (2, 1, 3, 4, 2)
# print(tup)
# print(type(tup))
# print(tup[0])
# # tup[0] = 6 Not allowed tuple is immutable
# tup2 = ()
# print(type(tup2))
# tup3 = (1) # treat as a integer
# print(type(tup3))
# tup4 = (1,) # treat as a tuple
# print(type(tup4))

# # methods
# print(tup.index(3)) # returns index of an element
# print(tup.count(2)) # returns count of an element










# # Lecture 4
# # Dictionary and Sets

# # Dictionaries

# # dict["key"] : To Access Value on key

# info = {
#   "name" : "Het",
#   "age" : 20,
#   "isAdult" : True,
#   "subject" : ["Python", "Data Structures"],
#   "topics" : ("dictionary", "set")
# }
# print(info)
# print(type(info))
# print(info["name"])

# info["name"] = "student"
# info["surname"] = "Shah"
# print(info["name"])
# print(info)

# null_dict = {}
# print(null_dict)

# # Nested Dictionaries
# students = {
#   "name" : "Rahul",
#   "subjects" : {
#     "physics" : 98,
#     "maths" : 96
#   }
# }
# print(students["subjects"])
# print(students["subjects"]["maths"])

# # methods
# print(students.keys())
# print(list(students.keys()))

# print(len(students))
# print(len(list(students.keys())))

# print(students.values())
# print(list(students.values()))

# print(students.items())
# print(list(students.items()))

# pairs = list(students.items())
# print(pairs[0])

# # print(students["name2"]) # error if no key is present
# print(students.get("name2")) # none if no key is present

# new_dict = {"city" : "Ahmedabad"}
# students.update(new_dict) # add the new key value pair in dictionary
# print(students)
# students.update({"name" : "Het"}) # override the value if key is existing
# print(students)
 
# # Sets
# nums = {1, 2, 3, 4, 4, 8, 7, 6, 12, 15}
# print(nums)
# print(type(nums))

# empty_set = set()
# print(empty_set)

# # methods
# nums.add(10)
# nums.add(9)
# nums.add("Hello")
# nums.add(("Hii", "World")) # sets are mutable but the items of sets are immutable
# # nums.add(["Hello","How are you?"]) # we can't add list into sets because they are mutable while items of sets are not
# nums.remove(8)
# print(nums)

# print(len(nums))
# # nums.clear() # empties the set
# # print(len(nums))

# collection = {"python", "coding", "program", "coder", 1, 2, 5, 8, 12, 15}
# print(collection)
# collection.pop()
# collection.pop() # remove any element of sets
# print(collection)

# # Union
# unioined = nums.union(collection) # combines both set value and returns new
# print(unioined)
# intersected = nums.intersection(collection) # combines common value and returns new
# print(intersected)  









# # Lecture 5 
# # Loops

# # while loop
# # count = 1
# # while count <= 5:
# #   print("Hello")
# #   count += 1
# # print(count)

# # i = 1
# # while i <= 100:
# #   print("World", i)
# #   i += 1

# # Print Numbers from 1 to 5
# i = 1
# while i <= 5:
#   print(i)
#   i += 1
# print("---------------")

# # Print Numbers from 5 to 1
# i = 5
# while i >= 1:
#   print(i)
#   i -= 1
# print("--------------")

# # Break 
# i = 5
# while i >= 1:
#   if i == 3:
#     break
#   print(i)
#   i -= 1
# print("-----------")

# # Continue
# i = 5
# while i >= 1:
#   if i == 3:
#     i -= 1
#     continue
#   print(i)
#   i -= 1
# print("-------")

# # for loops
# lst = [1, 2, 3]
# for val in lst:
#   print(val)
# print("----------")

# tup = (1, 2, 3, 5, 7, 6)
# for val in tup:
#   print(val)
# print("------------")

# str = "Hello"
# for char in str:
#   if(char=="o"):
#     print("O Found")
#     break
#   # print(char)
# else:
#   print("O not found") # does not execute if loop break executes

# # range function for loop

# for i in range(10):
#   print(i)
# print("--------")

# for i in range(1,5):
#   print(i)
# print("---------")

# for i in range(2, 10, 2):
#   print(i)
# print("--------")

# Pass

# for i in range(1, 5):
#   pass
# print("Hello")

# Lecture 6 
# Functions and Recursion

# a = 5
# b = 10
# sum = a + b
# print(sum) when we want to sum on other numbers we have to repeat logic 

# # Function Definition
# def sumCalculation(a, b): # (param1, param2)
#   sum = a + b
#   return sum

# print(sumCalculation(2,3)) # Function Call
# print(sumCalculation(5,10)) # (arg1, arg2)
# print(sumCalculation(7,3))
# print(sumCalculation(2,9))

# def printHello():
#   print("Hello")

# printHello()
# # print(printHello())

# # avearge of 3  
# def avg(a, b, c):
#   return ((a + b + c)/3)

# print(avg(10,20,50))

# # Default Argument
# def calcProduct(a, b=2):
#   return a*b

# print(calcProduct(5))

# # Recursion

# # print n to 1 backwards
# def show(n):
#   if(n == 0): # Base Case
#     return
#   print(n)
#   show(n-1)

# show(8)

# # factorial of n
# def fact(n):
#   if(n==0 or n==1):
#     return 1
#   return n * fact(n-1)

# print(fact(5))









# # Lecture 7 
# # File Input/Output

# # Text File : .txt, .docx, .log 
# # Binary File : .mp4, .mov, .png, .jpeg

# # r for read
# # w for write(overwrite)
# # x for create new file and open for write
# # a for append
# # b for binary mode
# # t for text mode
# # + for open disk file for updating

# # text mode is default if we want to read binary we have to combine r and b as rb

# # read file
# with open("demo.txt", "r") as file:
#   # data = file.read() # read whole file
#   # data = file.read(5) # read first 5 words
#   # print(data)
#   # print(type(data))
#   line1 = file.readline() # read first line
#   print(line1)
#   line2 = file.readline() # read first line
#   print(line2)
#   file.close()
# print("Closed File")

# # write file
# with open("demo.txt", "a") as file:
#   data = "\nI will try my best"
#   file.write(data)
#   file.close()


# # read + write
# with open("demo.txt", "r+") as file:
#   # data = "\Trying New Things"
#   # file.write(data)
#   print(file.read())
#   file.close()
#   # r+ : read + overwrite (start) no truncate
#   # w+ : read + overwrite (start) truncate
#   # a+ : read + append (end) no truncate

# Delete a file
# import os
# os.remove("temp.txt")









# # Lecture 8 OOPS

# # Class and Objects
# class Student:  
#   fullName = "anonymous" # Class Attribute
#   # collegeName = "Indus University" 

#   # Default Constructor
#   def __init__(self):
#     print("Hello")

#   # Parameterized Constructor which overrides default one
#   def __init__(self, fullName, marks):
#     self.fullName = fullName # self is reference of current object which represents instance attribute
#     self.marks = marks

#   def printName(self):
#     print("Name : ", self.fullName)

#   def printMarks(self):
#     print("Marks : ", self.marks)

#   # static methods : don't use self parameter and works on class level
#   @staticmethod
#   def college():
#     print("College Name : Indus")

# s1 = Student("Het", 99)

# # print(s1.fullName)
# # print(s1.marks)

# # s2 = Student("Arjuna", 99)
# # print(s2.fullName)
# # print(s2.marks)

# # print(Student.collegeName) # class attribute can be accessed by class name
# # print(s1.collegeName)
# # print(s2.collegeName)

# # print(s1.fullName) # print object attribute value because it has higher precedence 
# # class and object attribute can be same

# s1.printName()
# s1.printMarks()
# s1.college()


# # Abstraction : Hiding unnecessary details
# class Car:
#   def __init__(self):
#     self.acc = False
#     self.brk = False
#     self.clutch = False
  
#   def start(self):
#     self.clutch = True
#     self.acc = True
#     print("Car Started")

# car1 = Car()
# car1.start()

# # Encapsulation : Wrap data and functions into single unit









# # Lecture 9
# # del keyword : delete object or object props

# class Student:
#   def __init__(self, name):
#     self.name = name 

# s1 = Student("Het")
# print(s1.name)
# del s1
# print(s1)

# Private Attributes : __ in front of data
class Account:
  def __init__(self, acc_no, pwd):
    self.acc_no = acc_no
    self.__pwd = pwd # Private Property
  
  def show_pass(self):
    print(self.__pwd)

acc1 = Account(101, "Het@2005")
print(acc1.acc_no)
# print(acc1.__pwd) # can't acess outside class
acc1.show_pass()

class Person:
  # __name = "anonymous"
  def __hello(self): # Private Method
    print("Hello")

  def welcome(self):
    self.__hello()

p1 = Person()
p1.welcome()

# Single Inheritance

class Car:
  def __init__(self, type):
    self.type = type
  @staticmethod
  def start():
    print("Car Started")
  
  @staticmethod
  def stop():
    print("Car Stopped")

class Toyota(Car):
  def __init__(self, name, type):
    # super method used to access methods of parent class
    super().__init__(type)
    super().start()
    self.name = name

c1 = Toyota("Prius", "Electric")
print(c1.name)
print(c1.type)

# car1 = Toyota("Fortuner")
# car2 = Toyota("Prius")

# print(car1.name)
# car1.start()

# Multi Level Inheritance
class Fortuner(Toyota):
  def __init__(self, type):
    self.type = type

# car1 = Fortuner("Diesel")
# car1.start()

# Multiple Inheritance
class A:
  varA = "Welcome to A"
class B:
  varB = "Welcome to B"
class C(A, B):
  varC = "Welcome to C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# class Method : bound to class & receive class as implicit first argument
class Person:
  name = "anonymous"
  # def changeName(self, name):
  #   self.name = name # new name created inside object, does not chnage class attribute
  #   Person.name = name # 1st way that chnages class attribute
  #   self.__class__.name = name # 2nd way that changes class attribute

  @classmethod
  def changeName(cls, name):
    cls.name = name # change actual class variable name


p1 = Person()
print(p1.name)
p1.changeName("Het")  
print(p1.name) 
# print(Person.name)

# Property Decorator
class Student:
  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math
    # self.pct = str((self.phy + self.chem + self.math)/3) + " %"
  
  # def calculatePCT(self): # first approach to change calculated attribute value
  #   self.pct = str((self.phy + self.chem + self.math)/3) + " %"

  @property # second approch evereytime any attribute change, the value of percentage changes
  def percentage(self):
    return (str((self.phy + self.chem + self.math)/3) + " %")

s1 = Student(98, 97, 99)
# print(s1.pct)
print(s1.percentage) 

# we want to change phy marks it can be change directly but pct is calculated from initial marks so it does not changed 
s1.phy = 86
# print(s1.pct)
# s1.calculatePCT() # 1st approach
# print(s1.pct)
print(s1.percentage)

# Polymorphism : Single thing have multiple forms

# Operator Overloading : same operator have different meaning according to context

# Implicit Overloading
print(1 + 2) # Addition
print("Hello" + "World") # Concetenate
print([1, 2, 3] + [4, 5, 6]) # Merge

# + have different meaning in above case, example of polymorphism same thing different meaning

# Explicit Overlaoding
# Complex Numbers : Real Number + Imaginary Number like 3i + 4j