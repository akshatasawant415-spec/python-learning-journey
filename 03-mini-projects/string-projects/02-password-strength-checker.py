password=input("Enter your password :")
length=len(password)
uppercase=False
lowercase=False
for i in password:
    if i.isupper():
        uppercase=True
    elif i.islower():
        lowercase=True
digit=False
special_char=False
for i in password:
    if i.isdigit():
        digit=True
    elif not i.isalnum() and not i.isspace():
        special_char=True
if len(password)<8:
    print("Weak password")
elif uppercase and lowercase and digit and special_char!=False:
    print("Strong password")
else:
    print("Medium password")