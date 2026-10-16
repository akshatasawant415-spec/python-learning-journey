# 15. Find the sum of digits of a number
num=int(input("Enter a number:"))
num=abs(num)
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("Sum of digits=",sum)