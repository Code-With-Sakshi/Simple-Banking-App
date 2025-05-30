import os

class bank_balance:
    def __init__(self, account_holder, account_no, balance=45000):
        self.account_holder = account_holder
        self.account_no = account_no
        self.balance = balance
        self.filename = "Atm.txt"

        # Check if file exists and retrieve last balance if present
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                lines = f.readlines()
                for line in reversed(lines):
                    if f"{account_holder} (Acc No: {account_no})" in line and "New balance:" in line:
                        try:
                            self.balance = int(line.strip().split(":")[-1])
                            break
                        except ValueError:
                            pass

    def check_balance(self):
        print("Your balance:", self.balance)
        with open(self.filename, "a") as f:
            f.write(f"Checked balance: {self.balance}\n")

    def deposit(self):
        num = int(input("Amount to deposit: "))
        self.balance += num
        print(f"Deposited {num}. New balance is {self.balance}")
        with open(self.filename, "a") as f:
            f.write(f"Deposited {num}. New balance: {self.balance}\n")

    def withdraw(self):
        num = int(input("Amount to withdraw: "))
        if num <= self.balance:
            self.balance -= num
            print(f"Withdrew {num}. New balance is {self.balance}")
            with open(self.filename, "a") as f:
                f.write(f"Withdrew {num}. New balance: {self.balance}\n")
        else:
            print("Insufficient funds.")

# Input from user
acc_hold = input("Enter account holder name: ")
acc_no = int(input("Enter account number: "))

obj = bank_balance(acc_hold, acc_no)

# Start of transaction
with open("Atm.txt", "a") as f:
    f.write(f"\n--- Transaction History for {acc_hold} (Acc No: {acc_no}) ---\n")

# Menu loop
while True:
    print("1 = Check bank balance\n2 = Deposit\n3 = Withdraw\n4 = Quit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        obj.check_balance()

    elif choice == 2:
        obj.deposit()

    elif choice == 3:
        obj.withdraw()

    elif choice == 4:
        print("Do you want to quit? (y/n)")
        confirm = input().lower()
        if confirm == 'y':
            print("Exiting program. Thank you!")
            break
        else:
            continue
    else:
        print("Invalid choice.")

# Show transaction history
print("\n----- Transaction History from Atm.txt -----")
with open("Atm.txt", "r") as f:
    content = f.read()
    print(content)
