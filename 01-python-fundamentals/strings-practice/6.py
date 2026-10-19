# Q6. Check whether a string starts with a given substring.

text = input("Enter a string: ")
substring = input("Enter the substring to check: ")

result = text.startswith(substring)

print("Starts with substring:", result)