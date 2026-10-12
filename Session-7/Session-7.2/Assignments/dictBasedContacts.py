# Create a dictionary based program to manage contacts

import sys
contacts = {}

# # add
# name = input("Enter Name : ")
# contact = int(input("Enter Number : "))
# contacts[name] = contact
# print(contacts)

# # view
# print("Name ---------- Phone No")
# for key in contacts:
#   print(key, "----------", contacts[key])

# # search
# searchItem = input("Enter Name for Search : ")
# found = 0
# for key in contacts:
#   if(key == searchItem):
#     found = 1
#     print("Contact Found : ", key, "----",contacts[key])
# if(found == 0):
#   print("Contact Not Found")

# # update
# updateItem = input("Enter Name for Number Update : ")
# updateNum = input("Enter Number for Update : ")
# for key in contacts:
#   if(key == updateItem):
#     contacts[key] = updateNum
#     print(key, "----",contacts[key])

# # delete : This logic gives error : while iterating over dictionary we can't chnage the size of sictionary

# deleteItem = input("Enter Name for Delete : ")
# for key in contacts:
#   if(key == deleteItem):
#     contacts.pop(key)
#     print(key, " is deleted")

def addContact():
  # add 
  name = input("Enter Name : ")
  contact = int(input("Enter Number : "))
  contacts[name] = contact

def viewContact():
  # view
  print("Name ---------- Phone-No")
  for key in contacts:
    print(key, "----------", contacts[key]) 

def searchContact():
  # search
  searchItem = input("Enter Name for Search : ")
  found = 0
  for key in contacts:
    if(key == searchItem):
      found = 1
      print("Contact Found : ", key, "----",contacts[key])
  if(found == 0):
    print("Contact Not Found")
  
# update
def updateContact():
  updateItem = input("Enter Name for Number Update : ")
  updateNum = input("Enter Number for Update : ")
  found = 0
  for key in contacts:
    if(key == updateItem):
      found = 1
      contacts[key] = updateNum
      print(key, "----",contacts[key])
  if(found == 0):
    print("Contact Not Found")

def deleteContact():
  # delete
  deleteItem = input("Enter Name for Delete : ")
  if(deleteItem in contacts):
    contacts.pop(deleteItem)
    print(deleteItem, "is deleted")
  else:
    print("Contact Not Found")
    
while True:
  print("---------Contact Management---------")
  print("1. Add Contact")
  print("2. View Contact")
  print("3. Search Contact")
  print("4. Update Number")
  print("5. Delete Contact")
  print("6. Exit")
  choice = int(input("Enter your Choice : "))
  match choice:
    case 1: addContact()
    case 2: viewContact()
    case 3: searchContact()
    case 4: updateContact()      
    case 5: deleteContact()      
    case 6:
            # exit
            print("Thank You!!")
            sys.exit(0)
    case _:
            print("Invalid Choice")
