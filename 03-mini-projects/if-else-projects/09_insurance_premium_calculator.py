#9: Insurance Premium Calculator
customer_name=input("Enter name of customer :")
age=int(input("Enter age of customer :"))
occupation=input("Enter occupation risk(high/Medium) :")
smoker=input("Smoker Yes/No :")
base_premium=10000
additional_charge=0
if age<18:
    eligibility="Not eligible" 
    print("Not eligible for insurance")
else:
    eligibility="Eligible"
    if age>50:
        additional_charge=additional_charge+5000
    if occupation=="High":
        additional_charge=additional_charge+7000
    elif occupation=="Medium":
        additional_charge=additional_charge+3000
    if smoker=="Yes":
        additional_charge=additional_charge+5000
final_premium=base_premium+additional_charge
if additional_charge>=10000:
    risk_message="High Risk Policy"
else:
    risk_message="Normal Risk Policy"
print("Customer name:", customer_name)
print("Eligibility: Eligible")
print("Base premium:", base_premium)
print("Additional charges:", additional_charge)
print("Final premium:", final_premium)
print("Risk message:", risk_message)