class Student:
  def __init__(self, name, age, marks):
       self.name=name
       self.age=age
       self.marks=marks
students=[]

while True:
  print("===== Student Management System =====")
  print("1. Add Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Update Marks")
  print("5. Delete Student")
  print("6. Exit")
  choice=int(input("Enter your choice "))
  if choice==1:
    print("You selected Add Student")
    name=input("Enter your name :")
    age=int(input("Enter your age :"))
    marks=int(input("Enter your marks :"))
    student = Student(name, age, marks)
    students.append(student)
    print("Student added successfully!!")
  elif choice==2:
    print("You selected View student")
    print("===== Students =====")
    for student in students:
        print("Name :",student.name)
        print("Age :",student.age)
        print("Marks :",student.marks)
  elif choice==3:
    print("you selected search students")
    search_name=input("Enter name you want to search :")
    found=False
    for student in students:
      
      if search_name==student.name:
        found=True
        print("Student Found")
        print("Name :",student.name)
        print("Age :",student.age)
        print("Marks :",student.marks)
        break
       
    if not found:
        print("Student not found")
  elif choice==4:
    print("You selected update marks")
    update_name=input("Enter name of student you want to update :")
    found=False
    for student in students:
      if update_name==student.name:
        found=True
        print("The current marks are :",student.marks)
        new_marks=int(input("Enter the new marks :"))
        student.marks=new_marks
        print("The marks opdated successfully! ")
        print("New marks :",new_marks)
        break
    if not found:
      print("Student not found ")
  elif choice==5:
    print("you selected delete student")
    delete_name=input("Enter name of student you want to delete :")
    found=False
    for student in students:
      if delete_name==student.name:
        found=True
        students.remove(student)
        print("Student removed successfully!")
        break
    if not found:
        print("Student not found")
  elif choice==6:
    print("Thank you for using Student Management System!")
    break
  else:
    print("Invalid operation")