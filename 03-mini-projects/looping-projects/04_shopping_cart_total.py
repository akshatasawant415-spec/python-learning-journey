number_of_pro=int(input("Enter number of products :"))
if number_of_pro<=0:
    print("Invalid products number ")
    exit()
subtotal=0
discount=0
delivery_charge=0
for i in range(number_of_pro):
    price=float(input("Enter product price :"))
    quantity=int(input("Enter quantity :"))
    if price <0 or quantity <0:
        price("Invaild price and quantity")
        break
    item_total=price*quantity
    subtotal=subtotal+item_total
if subtotal>=3000:
    discount=subtotal * 10 /100
else:
    discount=0
amount_after_discount=subtotal-discount
if amount_after_discount<1500:
        delivery_charge=100
else:
    delivery_charge=0
final_payable=amount_after_discount+delivery_charge
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Delivery charge:", delivery_charge)
print("Final payable:", final_payable)
