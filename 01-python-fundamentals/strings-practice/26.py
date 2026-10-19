# Q26. Find the first and last occurrence of a character.

text = input("Enter a string: ")
character = input("Enter a character to find: ")

first=text.find(character)
last=text.rfind(character)

print("The first occurence :",first)
print("The last occuremce :",last)
