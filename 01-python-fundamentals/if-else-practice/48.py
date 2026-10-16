# 48. Language Choice Using Match Case
choice = int(input("Choose language: "))

match choice:
    case 1:
        print("English")
    case 2:
        print("Hindi")
    case 3:
        print("Marathi")
    case 4:
        print("French")
    case _:
        print("Invalid choice")