# 43. Calculate the sum of cubes of the first n number
n=int(input("Enter value of n :"))
total=0
for i in range(1,n+1):
    total=total+i * i * i
print("sum of cube is =",total)