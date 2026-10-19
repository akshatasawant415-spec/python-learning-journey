# Q20. Remove all occurrences of a given character from a string.

text = input("Enter a string: ")
character = input("Enter the character to remove: ")
result=text.replace(character,"")
print("Modified string :",result)