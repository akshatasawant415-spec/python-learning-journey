days = int(input("Enter number of days: "))
if days<=0:
    print("Invalid days")
else:
    total_expense = 0
    highest_expense = 0
    for day in range(days):
        expense=float(input(f"Enter expense for day {day+1} :"))
        total_expense=total_expense+expense
        if expense>highest_expense:
            highest_expense=expense
    average_expense=total_expense/days
    print("Total expense :",total_expense)
    print("Average daily expense :",average_expense)
    print("Highest daily expense :",highest_expense)
    if total_expense>5000:
        print("Budget Alert")
    else:
        print("Within budget")
