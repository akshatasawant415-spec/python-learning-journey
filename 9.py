class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

stu1=Student("Akshata",20)
print(stu1.name)
print(stu1.age)       

class Car:
    def __init__(self,Brand,Model):
        self.Brand=Brand
        self.Model=Model
car1=Car("BMW","M3")
car2=Car("Porsche",911)
print(car1.Brand)
print(car1.Model)
print(car2.Brand)
print(car2.Model)
    
class Dog:
    def Bark(self):
        print("Woof!")
d1=Dog
d1.Bark()

class Rectangle:
    def area(self):
        l=10
        b=5
        return (l*b)
r1=Rectangle
r1.area()
print(r1.area())

class BankAccount:
    def __init__(self,Name,Balance):
        self.Name=Name
        self.Balance=Balance
    def Deposit(self,amount):
        self.Balance+=amount
    def Withdraw(self,amount):
        if self.Balance>=amount:
           self.Balance-=amount
        else:
            print("Insufficient Balance")
    def show_balance(self):
        print("Available balance is : ",self.Balance)

acc=BankAccount("akshata",1000)
acc.Deposit(500)
acc.Withdraw(2000)
acc.show_balance()