class Expense:
    def __init__(self,category,amount,date):
        self.category=category
        self.amount=amount
        self.date=date
expenses=[]
while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Show Total Spending")
    print("6. Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        print("You selected to Add Expense ")
        category=input("Enter category of expense :")
        amount=int(input("Enter amount of expense :"))
        date=input("Enter date (DD/MM/YYYY): ")
        expense=Expense(category,amount,date)
        expenses.append(expense)
        print("The Expense added successfully!")
    elif choice==2:
        print("You have selected to View Expense ")
        print("===== Expense Tracker =====")
        for expense in expenses:
            print("Category is :",expense.category)
            print("The amount spent is :",expense.amount)
            print("The Date is :",expense.date)
    elif choice==3:
          print("You have selected to Search Expense ")
          search_category=input("Enter category you want to search :")
          found=False
          print("Expenses in list:")
          for expense in expenses:
             print(expense.category)
          for expense in expenses:

             if search_category==expense.category:
              found=True
              print("The category found ")
              print("The catgory is :",expense.category)
              print("The amount spent is :",expense.amount)
              print("The date is :",expense.date)
              break
          if not found:
              print("Category not found")
    elif choice==4:
        print("You have selected to Delete Expense ")
        delete_category=input("Enter the category you want to delete :")
        found=False
        for expense in expenses:
            if delete_category==expense.category:
                found=True
                expenses.remove(expense)
                print("Category removed succesfully !!")
                break
        if not found:
            print("Category not found ")        
    elif choice==5:
        print("You have slected to Show Total Expense ")
        total_expense=0
        for expense in expenses:
           total_expense+=expense.amount
           print("Total expense is :",total_expense)
    elif choice==6:
        print("You have selected Exit ")
        break
    else:
        print("Invalid Operation ")