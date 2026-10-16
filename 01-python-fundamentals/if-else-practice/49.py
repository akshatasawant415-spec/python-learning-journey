# 49. Result Status Using Match Case
status = input("Enter result status: ").lower()

match status:
    case "pass":
        print("Congratulations")
    case "fail":
        print("Better luck next time")
    case "absent":
        print("You were absent")
    case _:
        print("Invalid status")