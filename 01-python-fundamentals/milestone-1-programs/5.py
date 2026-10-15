#loops
for i in range(5):
    print("hello")
for i in range(1,21):
    print(i)
for i in range(0,20,2):
    print(i)
num=int(input("Enter a number: "))
for i in range(1,11):
    print(num*i)
while True:
    password=input("Enter password ")

    if password=="python123":
        break
print("Access Granted")
for i in range(1,20):
    if i==13:
        continue
    else:
        print(i)
for i in range(1,20):
    if i==15:
        break
    else:
        print(i)
