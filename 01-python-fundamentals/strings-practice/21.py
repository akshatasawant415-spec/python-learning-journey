# Q21. Find the length of a string without using len().

text = input("Enter a string: ")
count=0
for ch in text:
    count+=1
print("Length of string ",count)