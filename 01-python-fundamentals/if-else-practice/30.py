# 30. Single, Double or Three Digit
num = int(input("Enter a number: "))

if 0 <= num <= 9:
    print("Single digit")
elif 10 <= num <= 99:
    print("Double digit")
elif 100 <= num <= 999:
    print("Three digit")
else:
    print("More than three digits")