# 10 restaurant bill service
customer_name = input("Enter customer name: ")
food_bill = float(input("Enter food bill: "))
membership = input("Are you a member? (Yes/No): ")
discount = 0
service_charge = 0
if food_bill < 1000:
    discount = 0
elif food_bill < 3000:
    discount = food_bill * 5 / 100
elif food_bill < 5000:
    discount = food_bill * 10 / 100
else:
    discount = food_bill * 15 / 100
if membership=="Yes":
    discount=discount+food_bill * 5 /100
bill_after_discount = food_bill - discount
service_charge = bill_after_discount * 5 / 100
final_bill = bill_after_discount + service_charge
print("Customer name:", customer_name)
print("Original food bill:", food_bill)
print("Total discount:", discount)
print("Service charge:", service_charge)
print("Final payable amount:", final_bill)

if final_bill >= 5000:
    print("Thank you for dining with us!")