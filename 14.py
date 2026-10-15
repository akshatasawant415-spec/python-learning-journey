#encapsulation
class BankAccount:
    def __init__(self):
        self.__balance=1000
    def show_balnce(self):
        print(self.__balance)
    def deposit(self,amount):
        self.__balance+=amount
        print(amount)
    def withdraw(self,amount):
        self.__balance-=amount
        print(amount)
    
a1=BankAccount()
a1.show_balnce()
a1.deposit(1000)
a1.withdraw(500)
a1.show_balnce()

class Student:
    def __init__(self):
        self.__marks=90
    def update_marks(self,new_marks):
        if 0 < new_marks < 100:
            self.__marks=new_marks
        else:
            print("Invalid marks")
s1=Student()
s1.update_marks(95)