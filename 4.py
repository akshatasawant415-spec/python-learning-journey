marks=95
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("Fail")
age=int(input("Enter your age :"))
if age<=10:
    print("Child")
elif age<=18:
    print("Teenager")
elif age<=45:
    print("Adult")
elif age<=50:
    print("senior")
else:
    print("Enter valid age")

correct_usern="Akshata"
correct_pass="python123"
username=input("enter username ")
password=input("enter password ")
if username== correct_usern and password==correct_pass:
    print("logic sucessful")
else:
    print("invalid credentials")

balance=int(input("Enter balance amount "))
withdraw_amount=int(input("enter amonut for withdrawl :"))
if balance>=withdraw_amount:
    remainning_balance=balance-withdraw_amount
    print("Withdrwal succesful remaining amount ",remainning_balance)
else:
    print("insufficient balance")

#Movie ticket
age=int(input("Enter your age :"))
if age>=18:
    id=input("do you have ID?(y/n) ")
    if(id=="y"):
        print("Allow Entry")
    else:
        print("Rejected")
else:
    print("You cant go get id ")

        