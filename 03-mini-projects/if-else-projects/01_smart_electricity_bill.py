# Mini Project 1: Smart Electricity Bill Calculator

customer_name = input("Enter customer name: ")
units = int(input("Enter electricity units consumed: "))
energy_charge = 0
service_charge = 150

# Calculate the energy charge using if-elif-else
if units<0:
    print("Invalid units")
elif units<=100:
    energy_charge=units*3
    print("The energy charge is :",energy_charge)
elif units<=200:
    energy_charge = 100 * 3 + (units - 100) * 5
    print("The engrgy charge is :",energy_charge)
elif units>200:
    energy_charge=100*3 +100 * 5 + (units-200)*7
    print("The energy charge is :",energy_charge)
else:
    print("Invalid units")
final_bill=energy_charge+service_charge
print("Customer Name:", customer_name)
print("Units Consumed:", units)
print("Energy Charge:", energy_charge)
print("Service Charge:", service_charge)
print("Final Bill:", final_bill)
if final_bill > 5000:
    print("High Usage Bill")