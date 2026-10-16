# 33. Loan Eligibility
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))

if age >= 21 and salary >= 25000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")