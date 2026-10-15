def greet():
    print("Welcome to Python")
greet()
greet()
greet()

def add(a,b):
    sum=a+b
    print(sum)
add(10,20)

def square_1(num):
    square=num*num
    print(square)
num=int(input("Enter a number :"))
square_1(num)

def greet_1(name):
    print("Hello",name)
name=input("Enter a name :")
greet_1(name)

def is_adult(age):
    if age>=18:
        print("Adult")
    else:
        print("Child")
age=int(input("Enter your age :"))
is_adult(age)

def calculator(num1,num2,operator):
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
    else:
        print("invalid")
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
operator=input("Enter the operation :")
calculator(num1,num2,operator)
