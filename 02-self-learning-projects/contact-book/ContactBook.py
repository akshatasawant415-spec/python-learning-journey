class Contact:
    def __init__(self,name,number,email):
        self.name=name
        self.number=number
        self.email=email
contacts=[]
while True:
    print("===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save Contacts")
    print("7. Load Contacts")
    print("8. Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        print("You have selected to Add contact")
        name=input("Enter the name :")
        number=int(input("Enter your contact number :"))
        email=input("Enter your email :")
        contact=Contact(name,number,email)
        contacts.append(contact)
        print("The contact added successfully !!")
    elif choice==2:
        print("You have selected to View contact")
        print("===== Contact Book =====")
        for contact in contacts:
            print("The name is :",contact.name)
            print("The number is :",contact.number)
            print("The email is :",contact.email)
    elif choice==3:
        print("You have selected to Search contact")
        search_name=input("Enter name you want to search in contact book :")
        found=False
        for contact in contacts:
            if search_name==contact.name:
                found=True
                print("Contact found")
                print("The name is ",contact.name)
                print("The number is :",contact.number)
                print("The email is :",contact.email)
                break
        if not found:
            print("Contact not found")
    elif choice==4:
        print("You have selected to update contact")
        search_name=input("Enter name you want to search in contact book :")
        found=False
        for contact in contacts:
            if search_name==contact.name:
                found=True
                print("Contact found")
                print("What do you want to update?")
                print("1. Name")
                print("2. Number")
                print("3. Email")
                choice2=int(input("Enter you choice :"))
                if choice2==1:
                    print("You have selecte to update name ")
                    print("Current name is :",contact.name)
                    new_name=input("Enter new name :")
                    contact.name=new_name
                    print("The name updated sucessfully!!")
                    print("New name is :",new_name)
                    break
                elif choice2==2:
                    print("You have selected to update the number ")
                    print("Current number is :",contact.number)
                    new_number=int(input("Enter new number :"))
                    contact.number=new_number
                    print("The number updated successfully !!","New number is",new_number)
                    break
                elif choice2==3:
                    print("You have selected to update email ")
                    print("Current email is",contact.email)
                    new_email=input("Enter new email ")
                    contact.email=new_email
                    print("The email updated successfully!!","New email is",new_email)
                    break
                else:
                    print("Invalid choice")
        if not found:
            print("Contact name not found")

                
    elif choice==5:
        print("You have selected to delete contact")
        delete_name=input("Enter contact name you want do delete ")
        found=False
        for contact in contacts:
            if delete_name==contact.name:
                found=True
                contacts.remove(contact)
                print("contact removed successfully!!")
                break
        if not found:
            print("Contact not found")
    elif choice==6:
        print("You have selcted to save contact")
        with open("Contactbook.txt","w") as f:
            for contact in contacts:    
              f.write(contact.name + "," + str(contact.number) + "," + contact.email + "\n")                                  
    elif choice==7:
        print("You have selected to load contact")
        contacts.clear()
        try:

           with open("Contactbook.txt","r") as f:
            for line in f:
                con=line.split(",")
                print(con)
                print(con[0],con[1],con[2])
                contact=Contact(con[0],int(con[1]),con[2].strip())
                contacts.append(contact)
        except FileNotFoundError:
            print("File not found")
    elif choice==8:
        print("You have selected to Exit")
        break
    else:
       print("Invalid choice")
