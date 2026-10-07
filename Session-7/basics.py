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