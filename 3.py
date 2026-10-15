#operators
num1=int(input("enter a num "))
num2=int(input("enter a num "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**2)
print(num1**3)
num3=int(input("enter a number "))
if num3%2==0:
    print("even")
else:
    print("odd")
age=int(input("enter a age "))
if age>=18:
    print("is adult")
else:
    print("not adult")
username="Akshata"
password="python123"
entered_user="Akshata"
entered_password="python123"
is_user_correct=username==entered_user
is_pass_correct=password==entered_password
print("user name ",is_user_correct)
print("password ",is_pass_correct)
