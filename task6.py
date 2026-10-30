balance = 5000
withdrawal_limit = 2000

deposits = 0
withdrawals = 0
rejected = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        rejected += 1

    elif choice == 1:
        balance += amount
        deposits += 1
        print("Deposit successful")

    elif choice == 2:
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded")
            rejected += 1

        elif amount > balance:
            print("Insufficient balance")
            rejected += 1

        else:
            balance -= amount
            withdrawals += 1
            print("Withdrawal successful")

    else:
        print("Invalid transaction type")
        rejected += 1

print("\n----- ATM TRANSACTION SUMMARY -----")
print("Final Balance:", balance)
print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
print("Rejected Transactions:", rejected)

print("Thank you for using ATM")