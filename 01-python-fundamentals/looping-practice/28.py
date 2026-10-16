# 28. Check whether a number is Armstrong
num=int(input("Enter a number :"))
original=num
total=0
while num>0:
    digit=num%10
    total=total+digit**3
    num=num//10
if original==total:
    print("Armstrong number")
else:
    print("Not a armstrong number")