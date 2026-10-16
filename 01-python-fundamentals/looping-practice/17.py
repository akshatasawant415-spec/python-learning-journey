# 17. Find the largest digit in a number
num=int(input("Enter a nuumber :"))
largest=0
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
    num=num//10
print("Largest digit is =",largest)