correct_pin=1234
attempts=0
access_granted=False
while attempts<3:
    pin=int(input("Enter your pin :"))
    attempts=attempts+1
    entered_pin=pin
    if entered_pin==correct_pin:
            print("Access Grannted")
            access_granted = True
            break
    else:
       print("Incorrect pin")
if access_granted==False:
     print("Card Temporarily Locked")
print("Attempts used :",attempts)     
