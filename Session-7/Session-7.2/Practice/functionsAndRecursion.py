# # WAF to print length of list

# def getLength(lst):
#   return len(lst)

# lst1 = ["Ahmedabad", "Gandhinagar", "Vadodara", "Mumbai", "Chennai", "Delhi"]
# lst2 = ["Bengaluru", "Pune", "Hyderabad"]
# print(getLength(lst1))
# print(getLength(lst2))

# # WAF to print elements of list in single line
# def printList(lst):
#   for item in lst:
#     print(item, end = " ")
# printList(lst1)
# print()
# printList(lst2)

# # WAF to get factorial of n
# def fact(n):
#   ans = 1
#   for i in range(1, n):
#     ans *= i
#   return ans
# print(fact(5))
# print(fact(9))

# # WAF to convert USD to INR
# def USDtoINR(usd):
#   return usd*83

# usd = int(input("Enter Amount in USD : "))
# print("USD :", usd, "| INR :", USDtoINR(usd))

# # WAF to take number from user and print whethre it is odd or even

# def oddOrEven(n):
#   if(n%2 == 0):
#     return "Even"
#   else:
#     return "Odd"
# n = int(input("Enter a Number : "))
# print(oddOrEven(n))

# Recursion

# WARF to calculate sum of first n natural numbers
def sumOfN(n):
  if(n == 0):
    return 0
  return sumOfN(n-1) + n

n = int(input("Enter a Number : "))
print(sumOfN(n))

# WARF to print all elements of list
def printList(lst, index):
  if(index == len(lst)):
    return
  print(lst[index])
  printList(lst, index+1)

mylst = ["Apple", "Banana", "Chicku"]
printList(mylst, 0)