# 48. Check whether a number is a Strong number
num=int(input("Enter a number :"))
original=num
total=0
while num>0:
    digit=num%10
    fact =1
    for i in range(1,digit+1):
        fact=fact*i
    total=total+fact
    num=num//10
if original==total:
    print("Strong number")
else:
    print("Not astrong number ")