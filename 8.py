with open("hello.txt","r") as file:
   content= file.read()
print(content)

with open("students.txt","a") as file:
   name=input("Enter your name :")
   file.write(name)
with open("students.txt","r")as file:
   content1=file.read()
print(content1)

filename=input("Enter file to search :")
try:
   with open(filename,"r") as file:
      print("file opened ")
except:
   print("File not found")    

num=input("Enter your number :") 
try:
   number=int(num)
   print("you entered number :",num)
except:
   print("Invalid number")
with open("marks.txt","r") as file:
   file.read()
def save_marks(name,marks):
   try:
      with open("marks.txt","a") as file:
         print("saved ",name,marks)
   except:
      print("Not saved")
save_marks("Akshata",90) 
save_marks("Pranav",100)

with open("marks.txt","r") as file:
   con=file.read()
print(con)

with open("Demo.txt","r") as file:
   file.write("Hello")
   print(file.readline())

