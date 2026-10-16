#36. Find the sum of numbers entered until 0 is entered
total=0
while True:
    num=int(input("Enter a number (0 to stop ) :"))
    if num==0:
        break
    total=total+num
print("Sum=",total)