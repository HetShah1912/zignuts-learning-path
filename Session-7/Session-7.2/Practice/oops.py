# Create Student class that takes name and mark of 3 subjects as arguments, and gives average with method

class Student:
  def __init__(self, name, mathsMarks, physicsMarks, chemistryMarks):
    self.name = name
    self.mathsMarks = mathsMarks
    self.physicsMarks = physicsMarks
    self.chemistryMarks = chemistryMarks
  
  def printAvg(self):
    print("Average : ", ((self.chemistryMarks + self.mathsMarks + self.physicsMarks)/3))

name = input("Enter Name : ")
math = int(input("Enter Maths Marks : "))
phy = int(input("Enter Physics Marks : "))
chem = int(input("Enter Chemistry Marks : "))

s1 = Student(name, math, phy, chem)
s1.printAvg()

# Create Account class with 2 attributes - balance and account no, which have method for debit, credit and print the balance

class Account:
  def __init__(self, balance, acc_no):
    self.balance = balance
    self.acc_no = acc_no

  def debit(self, amount):
    self.balance -= amount
    print("Rs.",amount, " was Debited and now Total balance is : ", self.getBalance())

  def credit(self, amount):
    self.balance += amount
    print("Rs.",amount, " was Credited and now Total balance is : ", self.getBalance())

  def getBalance(self):
    return self.balance

acc1 = Account(10000, 101)
print("Account No : ",acc1.acc_no)
print("Balance : ",acc1.balance)

acc1.credit(100000)
acc1.debit(300000)