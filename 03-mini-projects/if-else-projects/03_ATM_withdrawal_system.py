# Mini Project 3: ATM Withdrawal System

account_holder = input("Enter account holder name: ")
balance = float(input("Enter current account balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))
maximum_limit=20000
if withdrawal_amount<=0:
    print("Enter valid withdrawal amount ")
elif withdrawal_amount>maximum_limit:
    print("Withdrawal limit is 20000 :")
elif withdrawal_amount>balance:
   print("Insufficient balance")
else:
  remaining_balance=balance-withdrawal_amount
  print("Remaining balance:", remaining_balance)
  print("Transaction successful!")
  if remaining_balance<1000:
    print("Low balance Warning")
remaining_balance=balance-withdrawal_amount
print("Account holder :",account_holder)
print("Remaining balance :",remaining_balance)
