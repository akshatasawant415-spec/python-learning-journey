# Q34. Find the ASCII value of each character in a string.

text = input("Enter a string: ")
for ch in text:
    print(ch,":",ord(ch))