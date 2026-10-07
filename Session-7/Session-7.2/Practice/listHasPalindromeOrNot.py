# WAP to check if a list contains a palindrome of elements or not

lst = [1, 2, 2, 1, 5]
copyLst = lst.copy()
print(copyLst)
copyLst.reverse()
if lst == copyLst:
  print("Elements of the list are Palindrome")
else:
  print("Elements of the list are not Palindrome")