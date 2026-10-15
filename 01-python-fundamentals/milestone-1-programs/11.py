try:
    age=int(input("Enter your age :"))
except :
    print("Please enter a valid number. ")
finally:
    print("Finally executed")

try:
    num1=int(input("Enter first number :"))
    num2=int(input("Enter second number :"))
    result=num1/num2
    print("Results :",result)
except ValueError:
    print("Invalid input ")
except ZeroDivisionError:
    print("You can not devide by zero ")

try:
    age=int(input("Enter your age :"))
except ValueError:
    print("Enter valid input ")

try:
    age=int(input("enter your age :"))
    if age < 0:
       raise ValueError("Age canot be negative ")
except ValueError as e:
    print(e)





