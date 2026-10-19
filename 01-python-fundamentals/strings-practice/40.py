# Q40. Count uppercase and lowercase letters separately.

text = input("Enter a string: ")

uppercase = 0
lowercase = 0
for ch in text:
    if ch.isupper():
        uppercase+=1
    elif ch.lower():
        lowercase+=1
print("Uppercase letters :",uppercase)
print("Lowercase letters :",lowercase)