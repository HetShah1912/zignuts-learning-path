# WAP to reverse a string withot inbuilt method

mystr = input("Enter a String : ")
reverse = ""
for i in range(len(mystr)-1, -1, -1):
  reverse += mystr[i]
print("Reveresed String is : ", reverse)

