# Q24. Extract only digits from a string.

text = input("Enter a string: ")
result=""
for ch in text:
    if ch.isdigit():
        result+=ch
print("Digits are :",result)