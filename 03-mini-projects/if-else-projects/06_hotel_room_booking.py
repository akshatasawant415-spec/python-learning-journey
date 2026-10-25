# 6 Hotel Room Booking System

guest_name=input("Enter guest name :")
room_type=input("Enter room type(Standard Deluxe Suite):")
number_of_nights=int(input("Enter number of nights :"))
discount=0
room_charge=0
if number_of_nights <= 0:
    print("Invalid number of nights")
elif room_type == "Standard":
    room_charge = number_of_nights * 2000

elif room_type == "Deluxe":
    room_charge = number_of_nights * 3500

elif room_type == "Suite":
    room_charge = number_of_nights * 6000

else:
    print("Invalid room type")
valid_booking = number_of_nights > 0 and room_type in ("Standard", "Deluxe", "Suite")
if valid_booking:
    if number_of_nights>=10:
        discount=room_charge*20/100
        print("The discount is :",discount)
    elif number_of_nights>=5:
        discount=room_charge*10/100
        print("The discount is :",discount)
    else:
        discount=0
        print("The discount is 0")
else:
    print("Invalid booking")
final_amount=room_charge-discount
print("THe guest name is :",guest_name)
print("The room typ is :",room_type)
print("The number of nights are :",number_of_nights)
print("The room charge is :",room_charge)
print("The discount is :",discount)
print("The final booking amount is :",final_amount)