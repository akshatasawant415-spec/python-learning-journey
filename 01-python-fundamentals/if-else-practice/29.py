# 29. Blood Donation Eligibility
age = int(input("Enter age: "))
weight = float(input("Enter weight: "))

if age >= 18 and weight >= 50:
    print("Eligible for blood donation")
else:
    print("Not eligible")