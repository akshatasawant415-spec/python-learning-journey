students = int(input("Enter number of students: "))
if students <= 0:
    print("Invalid number of students")
else:
    total_marks = 0
    pass_count = 0
    fail_count = 0
    for student in range(students):
        name = input("Enter student name: ")
        marks = float(input("Enter marks out of 100: "))
        if marks < 0 or marks > 100:
            print("Invalid marks")
        else:
            total_marks = total_marks + marks
            if marks >= 75:
                grade = "A"
            elif marks >= 60:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            elif marks >= 40:
                grade = "D"
            else:
                grade = "Fail"
            if marks >= 40:
                pass_count = pass_count + 1
            else:
                fail_count = fail_count + 1
            print("Student:", name)
            print("Marks:", marks)
            print("Grade:", grade)
    valid_students = students - fail_count
    if valid_students > 0:
        average = total_marks / (pass_count + fail_count)
        print("Class average:", average)
    print("Pass count:", pass_count)
    print("Fail count:", fail_count)
