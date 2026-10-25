#07_mobile_dataplan_bill

Customers_name=input("Enter name of Customer :")
Plan_type=input("Enter plan type(Basic,Standard,Premium) :")
Extra_data=int(input("Enter extra data used in GB :"))
bill=0
surcharge=0
if Plan_type not in ("Basic","Standard","Premium"):
    print("Invalid plan")
elif Plan_type=="Basic":
    bill=299
    included_data=10
elif Plan_type=="Standard":
    bill=499
    included_data=25
elif Plan_type=="Premium":
    bill=799
    included_data=50
Extra_data_charge=Extra_data*20
if Extra_data>10:
   surcharge=100
   print("Surcharge is 100rs",surcharge)
elif Extra_data<0:
    print("Surcharge cant be negative ")
final_bill=bill+Extra_data_charge+surcharge
print("Customer_name :",Customers_name)
print("Plan type :",Plan_type)
print("Base plan charge :",bill)
print("Extra data used is :",Extra_data)
print("Extra data charge:", Extra_data_charge)
print("Surcharge is ",surcharge)
print("Final bill is :",final_bill)