# Q25. Extract only alphabets from a string.

text = input("Enter a string: ")
result=""
for ch in text:
    if ch.isalpha():
        result+=ch
print("Alphabets :",result)