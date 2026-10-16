# 11. Count the number of digits in a number
num=int(input("Enter a number:"))
num=abs(num)
count=0
while num>0:
    count=count+1
    num=num//10
print("Number of digits=",count)