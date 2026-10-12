# Create a new file "practice.txt" and add some content to it
with open("practice.txt", "w") as file:
  file.write("Hello Everyone\n")
  file.write("I am learning python\n")
  file.write("I like programming\n")
  file.close()

with open("practice.txt", "r") as file:
  data = file.read()
  print(data)
  file.close()

# replace python to java
updatedData = data.replace("python", "java")
with open("practice.txt", "w") as file:
  file.write(updatedData)
  file.close()

# search if the word learning is present or not in file
word = "learning"
with open("practice.txt", "r") as file:
  data = file.read()
  if(data.find(word)):
    print("Found")
  else:
    print("Not Found")
  file.close()

# WAF to find in which line learning word occurs first, if not ocuur then return -1
def check_line():
  word = "programming"
  line_number = 1
  with open("practice.txt", "r") as file:
    line = file.readline()
    while line:
      if word in line:
        return line_number
      line_number += 1
      line = file.readline()
  return -1

print(check_line())

# From a file containing numbers seperated by comma, print count of even numbers
with open("numbers.txt", "w") as file:
  file.write("1, 2, 3, 8, 45, 67, 87")
  file.close()

with open("numbers.txt", "r") as file :
  nums = file.read()
  print(nums)
  even = 0

  # num = ""
  # for i in range(0, len(nums)):
  #   if nums[i] == ",":
  #     print(int(num))
  #     current = int(num)
  #     if current%2 == 0:
  #       even+=1
  #     num = ""
  #   else:
  #     num += nums[i]
  # if num:
  #   print(int(num))
 

  nums = nums.split(",")
  for val in nums:
    if(int(val)%2 == 0):
      even += 1
  print("Count of Even : ",even)