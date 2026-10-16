# 32. Exam Eligibility
attendance=float(input("Enter attendance percentage :"))
marks=int(input("Enter marks :"))
if attendance>=75:
    if marks >=40:
        print("Eligible for exam")
    else:
        print("Not eligible deu to low marks")
else:
    print("Not eligible deu to low attendance")