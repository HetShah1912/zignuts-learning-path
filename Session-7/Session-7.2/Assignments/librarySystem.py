# Write a class for a library system that allows adding/removing books and searching by
# title.
import sys
class Library:
  books = []
  def __init__(self, name):
    self.name = name

  def addBook(self, name):
    self.books.append(name)
    print(name, "Book is Added")
  
  def viewBooks(self):
    print("List of Books : ")
    for book in self.books:
        print(book) 
  
  def searchBook(self, name):
    if(name in self.books):
       print(name, "Book is Available")
    else:
       print(name, "Book Not Found")
  
  def removeBook(self, name):
    if(name in self.books):
      self.books.remove(name)
      print(name, "Book is removed")
    else:
      print(name,"Book Not Found")
    
library = input("Enter Library Name : ")
l1 = Library(library)

while True:
  print("---------Library Management System---------")
  print("1. Add Book")
  print("2. View Books")
  print("3. Search Book")
  print("4. Remove Book")
  print("5. Exit")

  choice = int(input("Enter your Choice : "))
  match choice:
    case 1: 
            book = input("Enter Book Name : ")
            l1.addBook(book)
    case 2: l1.viewBooks()
    case 3: 
            book = input("Enter Book you are looking for : ")
            l1.searchBook(book)
    case 4: 
            book = input("Enter Book Name for Removal : ")
            l1.removeBook(book)           
    case 5:
            # exit
            print("Thank You!!")
            sys.exit(0)
    case _:
            print("Invalid Choice")