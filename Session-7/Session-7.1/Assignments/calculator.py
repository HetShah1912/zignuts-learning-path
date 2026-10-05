#  Write a simple calculator that accepts two numbers and an operator (+, -, *, /) and prints
# the result

def calculator(num1, num2, operator):
  match operator:
    case "+": return num1 + num2
    case "-": return num1 - num2
    case "*": return num1 * num2
    case "/":
              if(num2 == 0):
                print("Can't Divide by 0")
                return
              return num1 / num2
    case _: 
             print("Enter Valid Operator")
             return

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
op = input("Enter Operator : ")
result = calculator(num1, num2, op)
print(f"Result is : {result}")