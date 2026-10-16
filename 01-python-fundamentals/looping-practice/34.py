#34. Check whether a string is palindrome
text=input("Enter a string :")
reverse=""
for ch in text:
    reverse=reverse+ch
if reverse==text:
    print("palindrome")
else:
    print("Not a palindrome")