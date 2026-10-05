# WAP to find sum of first n prime numbers
import math

def isPrime(n):
  if(n <= 1):
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if(n % i == 0):
      return False
  return True


def getSum(num):
  prime_sum = 0
  current_num = 2
  totalPrime = 0
  while totalPrime < num:
    if isPrime(current_num):
      print("Current Prime No. is : ", current_num)
      prime_sum += current_num
      totalPrime += 1
    current_num += 1
  return prime_sum

num = int(input("Enter a Positive Integer Number : "))
result = getSum(num)
print(f"The Sum of first {num} Prime Numbers is : {result}")