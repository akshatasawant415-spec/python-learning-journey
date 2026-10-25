# 08_movie_tracking_booking
Customer_name = input("Enter name of customer: ")
Age = int(input("Enter age of the customer: "))
show_type = input("Enter show type (Morning, Evening): ")
day_type = input("Enter day type (Weekday, Weekend): ")
base_ticket = 200
discount = 0
extra_charge = 0

if Age < 0:
    print("Invalid age")
else:
    if Age < 12:
        discount = base_ticket * 50 / 100
    elif Age >= 60:
        discount = base_ticket * 30 / 100
    if show_type == "Morning":
        discount = discount + 30
    if day_type == "Weekend":
        extra_charge = 50
    final_ticket = base_ticket - discount + extra_charge
    print("Customer name:", Customer_name)
    print("Original ticket price:", base_ticket)
    print("Discount:", discount)
    print("Weekend surcharge:", extra_charge)
    print("Final ticket price:", final_ticket)