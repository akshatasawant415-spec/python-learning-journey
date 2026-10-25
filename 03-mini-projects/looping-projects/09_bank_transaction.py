balance = float(input("Enter opening balance: "))
number_of_transactions = int(input("Enter number of transactions: "))

deposit_count = 0
successful_withdrawals = 0
rejected_withdrawals = 0

if balance < 0 or number_of_transactions <= 0:
    print("Invalid input")
    exit()

for i in range(number_of_transactions):
    transaction_type = input("Enter deposit or withdrawal: ").strip().lower()
    amount = float(input("Enter transaction amount: "))

    if amount <= 0:
        print("Invalid transaction amount")

    elif transaction_type == "deposit":
        balance = balance + amount
        deposit_count = deposit_count + 1

    elif transaction_type == "withdrawal":
        if amount <= balance:
            balance = balance - amount
            successful_withdrawals = successful_withdrawals + 1
        else:
            print("Insufficient balance")
            rejected_withdrawals = rejected_withdrawals + 1

    else:
        print("Invalid transaction type")

print("Final balance:", balance)
print("Total deposits:", deposit_count)
print("Successful withdrawals:", successful_withdrawals)
print("Rejected withdrawals:", rejected_withdrawals)

if balance < 1000:
    print("Warning: Balance is below ₹1000")
