# WAP to find the greatest of 3 entered by user
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))

if(num1 > num2 and num1 > num3):
  print(num1, "is greater")
elif(num2 > num3):
  print(num2, "is greater")
else:
  print(num3, "is greater")