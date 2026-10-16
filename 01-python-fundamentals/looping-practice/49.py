# 49. Display a menu-driven program using while loop
while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Division")
    print("5.exit")

    choice=int(input("Enter your choice :"))
    if choice==1:
        a=int(input("Enter first number :"))
        b=int(input("Enter second number :"))
        print("Sum=",a+b)
    elif choice==2:
        a=int(input("Enter first number :"))
        b=int(input("Enter second number :"))
        print("Subtraction=",a-b)
    elif choice==3:
        a=int(input("Enter first number :"))
        b=int(input("Enter second number :"))
        print("Multiplication=",a*b)
    elif choice==4:
        a=int(input("Enter first number :"))
        b=int(input("Enter second number :"))
        print("Division=",a/b)
    elif choice==5:
        print("Exiting program")
    else:
        print("Invalid choice")