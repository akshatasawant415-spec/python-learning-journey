# 40. Valid Password Using Nested If
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Invalid username")