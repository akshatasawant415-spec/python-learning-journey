# 50. Simple ATM Menu
choice=int(input("Enter your choice:"))

match choice:
    case 1:
        print("Check balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("deposit Money")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice ")