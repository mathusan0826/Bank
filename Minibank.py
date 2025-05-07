import datetime
import os

# ---------------- Admin Login ---------------- #
admin_username = "M"      # Example: Manager
admin_password = "0"      # Example: 0826

# Ask for login
user_input = input(" Enter Admin Username: ")
pass_input = input(" Enter Admin Password: ")

# Check if login is correct
if user_input == admin_username and pass_input == admin_password:
    print("\n Welcome! Login Successful.")
else:
    print(" Wrong username or password. Try again.")
    exit()

# ---------------- Data ---------------- #
# These are in-memory data stores (used while the program is running)
customers = {}           # {customer_id: customer_data}
transactions = {}        # {customer_id: [list of transactions]}
balances = {}            # {customer_id: [balance history]}

# Make sure files exist before using them
for filename in ["Customer.txt", "User.txt", "Bankaccount.txt", "Transaction.txt"]:
    if not os.path.exists(filename):
        open(filename, 'w').close()

# ---------------- Functions ---------------- #

# 1. Register new customer (basic info)
def register_customer():
    print("\n Register New Customer")
    name = input("Name: ")
    age = input("Age: ")
    address = input("Address: ")
    phone = input("Phone: ")
    nic = input("NIC: ")
    email = input("Email: ")

    with open("Customer.txt", 'a') as file:
        file.write(f"{name}\t{age}\t{address}\t{phone}\t{nic}\t{email}\n")

    print(" Customer Registered Successfully.")

# 2. Create Bank Account for customer
def create_account():
    try:
        print("\n Create New Account")
        customer_id = int(input("Customer ID (number): "))
        if customer_id in customers:
            print(" ID already exists.")
            return

        name = input("Name: ")
        address = input("Address: ")
        nic = input("NIC: ")
        phone = input("Phone: ")
        email = input("Email: ")
        starting_balance = float(input("Starting Balance (Rs): "))
        acc_number = input("Account Number (e.g., 004): ")

        customers[customer_id] = {
            "name": name,
            "address": address,
            "nic": nic,
            "phone": phone,
            "email": email,
            "balance": starting_balance,
            "account_id": acc_number
        }

        balances[customer_id] = [f"{datetime.datetime.now()} | Balance: ₹{starting_balance}"]

        with open("User.txt", 'a') as f:
            f.write(f"{customer_id}\t{name}\t₹{starting_balance}\n")

        with open("Bankaccount.txt", 'a') as f:
            f.write(f"{customer_id}\t{name}\t{acc_number}\t₹{starting_balance}\n")

        print(f" Account created for {name} with ₹{starting_balance}")

    except ValueError:
        print(" Invalid input. Please use numbers where needed.")

# 3. Deposit money to account
def deposit_money():
    try:
        print("\n Deposit Money")
        customer_id = int(input("Customer ID: "))
        if customer_id in customers:
            amount = float(input("Amount to deposit (Rs): "))
            customers[customer_id]["balance"] += amount

            log = f"{datetime.datetime.now()} | {customers[customer_id]['name']} | Deposit ₹{amount} | New Balance: ₹{customers[customer_id]['balance']}"
            transactions.setdefault(customer_id, []).append(log)
            balances.setdefault(customer_id, []).append(f"{datetime.datetime.now()} | ₹{customers[customer_id]['balance']}")

            with open("Transaction.txt", 'a') as f:
                f.write(log + "\n")

            print(" Deposit successful.")
        else:
            print(" Customer not found.")
    except ValueError:
        print(" Please enter numbers only.")

# 4. Withdraw money
def withdraw_money():
    try:
        print("\n Withdraw Money")
        customer_id = int(input("Customer ID: "))
        if customer_id in customers:
            amount = float(input("Amount to withdraw (Rs): "))
            if customers[customer_id]["balance"] >= amount:
                customers[customer_id]["balance"] -= amount
                log = f"{datetime.datetime.now()} | {customers[customer_id]['name']} | Withdraw ₹{amount} | New Balance: ₹{customers[customer_id]['balance']}"
                transactions.setdefault(customer_id, []).append(log)
                balances.setdefault(customer_id, []).append(f"{datetime.datetime.now()} | ₹{customers[customer_id]['balance']}")

                with open("Transaction.txt", 'a') as f:
                    f.write(log + "\n")

                print(" Withdrawal successful.")
            else:
                print(" Not enough money.")
        else:
            print(" Customer not found.")
    except ValueError:
        print(" Please enter valid numbers.")

# 5. Show current balance
def check_balance():
    try:
        customer_id = int(input("\n Customer ID: "))
        if customer_id in customers:
            print(f" Balance: ₹{customers[customer_id]['balance']}")
        else:
            print(" Customer not found.")
    except ValueError:
        print(" Invalid ID.")

# 6. Show transaction history
def show_transaction_history():
    try:
        customer_id = int(input("\n Enter Customer ID: "))
        print(f"Transaction History for {customers.get(customer_id, {}).get('name', 'Unknown')}:")
        for t in transactions.get(customer_id, []):
            print(t)
    except ValueError:
        print(" Invalid input.")

# 7. Show balance history
def show_balance_history():
    try:
        customer_id = int(input("\n Enter Customer ID: "))
        print(f"Balance History for {customers.get(customer_id, {}).get('name', 'Unknown')}:")
        for b in balances.get(customer_id, []):
            print(b)
    except ValueError:
        print(" Invalid input.")

# 8. Delete customer account
def delete_account():
    try:
        customer_id = int(input("\n Customer ID to delete: "))
        if customer_id in customers:
            confirm = input(f"Are you sure you want to delete account for {customers[customer_id]['name']}? (yes/no): ")
            if confirm.lower() == "yes":
                del customers[customer_id]
                transactions.pop(customer_id, None)
                balances.pop(customer_id, None)

                with open("User.txt", 'w') as f:
                    for cid, data in customers.items():
                        f.write(f"{cid}\t{data['name']}\t₹{data['balance']}\n")

                with open("Bankaccount.txt", 'w') as f:
                    for cid, data in customers.items():
                        f.write(f"{cid}\t{data['name']}\t{data['account_id']}\t₹{data['balance']}\n")

                print(" Account deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print(" Customer ID not found.")
    except ValueError:
        print(" Invalid input.")

# ---------------- Main Menu ---------------- #
while True:
    print("******************************************\n ===== ATM MENU =====\n******************************************")
    print("1. Register New Customer")
    print("2. Create Bank Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Show Transaction History")
    print("7. Show Balance History")
    print("8. Delete Account")
    print("9. Exit")

    user_choice = input(" Choose option (1-9): ")

    if user_choice == "1":
        register_customer()
    elif user_choice == "2":
        create_account()
    elif user_choice == "3":
        deposit_money()
    elif user_choice == "4":
        withdraw_money()
    elif user_choice == "5":
        check_balance()
    elif user_choice == "6":
        show_transaction_history()
    elif user_choice == "7":
        show_balance_history()
    elif user_choice == "8":
        delete_account()
    elif user_choice == "9":
        print(" Goodbye! Thanks for using the ATM System.")
        break
    else:
        print(" Please enter a number between 1 and 9.")
