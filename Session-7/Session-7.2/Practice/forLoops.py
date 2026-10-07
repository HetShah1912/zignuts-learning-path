# Print elements using for loop and search for specific element

lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
x = 49
index = 0
for val in lst:
  if(val == x):
    print("Number Found on index : ", index)
    break
  # print(val)
  index += 1

# Print 1 to 100 using for loop
for i in range(1, 101):
  print(i)
print("---------")

# Print 100 to 1 using for loop
for i in range(100, 0, -1):
  print(i)
print("---------")

# Print multiplication table
n = int(input("Enter Number : "))
for i in range(1, 11):
  print(n, " * ", i, " * ", n*i)