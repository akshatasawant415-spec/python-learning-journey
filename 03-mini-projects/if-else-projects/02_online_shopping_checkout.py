# Mini Project 2: Online Shopping Checkout

customer_name = input("Enter customer name: ")
purchase_amount = float(input("Enter purchase amount: "))
customer_type = input("Enter customer type (Regular/Premium): ")

discount = 0
delivery_charge = 0
if purchase_amount>=5000:
    discount=purchase_amount * 20 /100
    print("The discount is :",discount)
elif purchase_amount>=3000:
    discount=purchase_amount * 10/100
    print("The discount is :",discount)
elif purchase_amount>=1000:
    discount=purchase_amount * 5/100
    print("The discount is :",discount)
else:
    discount=0
    print("No discount apllicable")
if customer_type.lower()=="premium":
    premium_discount=purchase_amount * 5 /100
    discount=discount+premium_discount
print("Total discount is :",discount)