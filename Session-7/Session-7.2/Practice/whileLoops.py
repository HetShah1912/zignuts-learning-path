# WAP to print 1 to 100

# i = 1
# while i <= 100:
#   print(i)
#   i += 1
# print("--------")

# WAP to print 100 to 1

# i = 100
# while i >= 1:
#   print(i)
#   i -= 1
# print("--------")

# WAP to print multiplication number of n

# n = int(input("Enter Number : "))
# i = 1
# while i <= 10:
#   print(n, " * ", i, " = ", n*i) 
#   i += 1
# print("---------------------")

# WAP to print square of 1 to 10

# i = 1
# while i <= 10:
#   print(i**2)
#   i += 1
# print("---------------------")

# WAP to search a number in previous tuple
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
length = len(nums)
i = 0
while i <= length-1:
  print(nums[i])
  i += 1 

numsTuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
search = int(input("Enter Number for Search : "))
lengthTuple = len(numsTuple)
i = 0
while i <= lengthTuple-1:
  if numsTuple[i] == search:
    print("Found at index : ", i)
    break
  else:
    print("Searching...")
  i += 1 