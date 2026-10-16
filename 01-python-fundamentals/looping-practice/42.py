# 42. Calculate the sum of squares of the first n numbers
n=int(input("Enter value of n :"))
total=0
for i in range(1,n+1):
    total=total+i*i
print("sum of squares=",total)