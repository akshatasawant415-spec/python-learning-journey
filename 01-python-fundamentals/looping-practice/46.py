# 46. Print the first n multiples of a number
num=int(input("Enter a number :"))
n=int(input("Enter a number of multiple :"))
for i in range(1,n+1):
    print(num*i)