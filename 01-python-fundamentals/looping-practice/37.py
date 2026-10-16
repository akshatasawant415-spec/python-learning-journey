#37. Print numbers until the user enters a negative number
while True:
    num=int(input("Enter a number :"))
    if num<0:
        break
    print(num)