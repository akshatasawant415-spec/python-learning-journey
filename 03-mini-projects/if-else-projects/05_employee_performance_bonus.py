# 5 Employee Performance Bonus

employee_name=input("Enter employee name :")
monthly_salary=int(input("Enter monthly salary :"))
performance_rating=input("Enter performance rating :")
bonus=0
if performance_rating=="5":
    bonus=monthly_salary*20/100
    print("The bonus is :",bonus)
elif performance_rating=="4":
    bonus=monthly_salary*15/100
    print("The bonus is :",bonus)
elif performance_rating=="3":
    bonus=monthly_salary*10/100
    print("The bonus is :",bonus)
elif performance_rating=="2":
    bonus=monthly_salary*5/100
    print("The bonus is :",bonus)
elif performance_rating=="1":
    bonus=0
    print("The bonus is :",bonus)
else:
    print("Enter rating between 1 to 5")
final_salary=monthly_salary+bonus
print(f"Salary of {employee_name} after bonus is : ",final_salary)
if performance_rating=="5":
    print("Excellent Performer")