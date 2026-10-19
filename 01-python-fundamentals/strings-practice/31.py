# Q31. Remove punctuation marks from a string.

import string

text = input("Enter a string: ")

result = ""
for ch in text:
    if ch not in string.punctuation:
        result+=ch
print("String without punctuation :",result)