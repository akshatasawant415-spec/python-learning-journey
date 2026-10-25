# Mini Project 4: Student Scholarship Eligibility

student_name=input("Enter students name :")
percentage=float(input("Enter students percentage :"))
anuual_family_income=int(input("Enter annual family income :"))
attendance=float(input("Enter attendence percentage :"))
if percentage>=75.0 and anuual_family_income<=400000 and attendance >=75.0:
    print("Eligible for scholarship ")
    if percentage>=90:
        print("Eligible for full scholarship")
    else:
        print("Eligible for partial scholarship")
else:
    print("Not eligible")
    if percentage<75.0:
        print("Reason :Percentage below 75%")
    if anuual_family_income>400000:
        print("Reason :High family income")
    if attendance<75.0:
        print("Reason :Attendance is low")