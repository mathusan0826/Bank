import datetime
import os

#*****Admin login*****
admin_username="Manager"
admin_password="0826"

#For login admin 
user_input=input("Enter admin Username: ")
pass_input=input("Enter admin password: ")

#Chake login adming condition
if user_input == admin_username and pass_input ==admin_password:
    print("\n welcome Login Successful.")
else:
    print("Wrong username or password please Try again.")
    exit()

#Data Store
customers = {}        #{customer_id: customer_data}
transaction ={}      #{customer_id :[list of transactions]}
balance ={}          #{customer_id :[balance history]}

#txt file creating
for filename in ["Customer.txt",
                 "User.txt",
                 "Bankaccount.txt",
                 "Transaction.txt"
                 ]:
    if not os.path.exists(filename):
        open(filename, 'w').close()

#functions Starting      
#Task 1 Register new customer
def register_customer():
      print("\n Register New Customer")
      name= input("Name: ")
      age = input("Age: ")
      address= input("Address: ")
      phone= input("Phone: ")
      nic= input("NIC: ")
      email= input("Email: ")

      with open(" Customer.txt", 'a') as file:
          file.write(f"{name}\t{age}\t{address}\t{phone}\t{nic}\t{email}\n")

      print("Customer Registered Successfully.")

#Task 2 Create Bank Account For user
def create_account():
    try:
        print("\n Create New Account")
        customer_id = int(input("Customer ID (number): "))
        if customer_id in customers:
             print(" ID already Exists") 
             return

        name = input("Name:")
        address =input("Adress:")
        nic = input("NIC:")
        phone = input("Phone:")
        email=input("Email:")
        starting_balance= float(input("Starting Balance(Rs):"))
        acc_number=input("Account Number:") #004

        customers[customer_id]={
            "name":name,
            "address":address,
            "nic":nic,
            "phone":phone,
            "email":email,
            "balance":starting_balance,
            "account_id":acc_number
        }

        balance[customer_id]=[f"{datetime.datetime.now()} |Balance:Rs{starting_balance}"]

        with open("User.txt", 'a') as f:
            f.write(f"{customer_id}\t{name}\tRs{starting_balance}\n")

        with open("Bankaccount.txt",'a') as f:
            f.write(f"{customer_id}\t{name}\t{acc_number}\tRs{starting_balance}\n")

        print(f"Account created for {name} with Rs{starting_balance}")

    except ValueError:
        print("Invalid input. Please use numbers.")

#Task 3 Deposit Money
def deposit_money():
    try:
        print("\n Deposit Money")
        customer_id=int(input("Customer ID:"))
        if customer_id in customers:
            amount =float(input("Amount to deposit (Rs):"))
            customers[customer_id]["balance"] == amount

            log=f"{datetime.datetime.now()} | {customers[customer_id]['name']} |Deposit Rs{amount} | New Balance: Rs {customers[customer_id][balance]}"
            transaction(customer_id,[]).append(log)
            balance.setdefoult(customer_id,[]).append(f"{datetime.datetime.now()}) | Rs{customers[customer_id]['balance']}")

            with open("Transaction.txt",'a') as f:
                f.write(log+ "\n")

            print("Deposit successful.")
        else:
            print("Customer not found.")
    except ValueError:
        print("Please enter number only.")  

# task 4 Withdraw money
def withdraw_money():
    try:
        print("\n Withdraw Money")
        customer_id=int(input("customer_id"))
        if customer_id in customers:
            amount=float(input("Amount to withdraw (Rs):"))
            if customers[customer_id]["balance"]>= amount:
                customers[customer_id]["balance"]>- amount
                log=f"{datetime.datetime.now()}|{customers[customer_id]['name']} |Withdraw Rs{amount} |New Balance: Rs{customers[customer_id]['balance']}"
                transaction.setdefault(customer_id, []).append(log)
                balance.setdefault(customer_id, [].append(f"{datetime.datetime.now()} | Rs{customers[customer_id]['balance']}")) #chake

                with open("Transation.txt", 'a') as f:
                    f.write(log + "\n")

                print("Withdrawal successful.")
            else:
                print("Not enough money.")
        else:
            print("Customer not found.")
    except ValueError:
        print("Please enter valid number.")

# task 5 Current balance
def check_balance():
    try:
        customer_id= int(input("\n Customer ID"))
        if customer_id in customers:
            print(f" Balance: Rs {customers[customer_id]['balance']}")
        else:
            print("Customer not found.")
    except ValueError:
        print("Invalid ID.")

#task 6 Show transaction History
def show_transaction_history():
    try:
        customer_id =int(input("\n Enter Customer ID:"))
        print(f"Transaction History for {customers.get(customer_id,{}).get('name','Unknown')}:")
        for b in transaction.get(customer_id, []):
            print(b)

    except ValueError:
        print("Invalid input.")



#task 7 show balance History
def show_balance_history():
    try:
        customer_id = int(input("\n Enter the customer ID: "))
        print(f"Balance History for{customers.get(customer_id,{}).get('name', 'unknow')}:")
        for b in balance.get(customer_id, []):
            print(b)
    except ValueError:
        print("Invalid input.") 

#task 8   
def delete_account():
    try:
        customer_id = int(input("\n Customer ID to delete: "))
        if customer_id in customers:
            confirm = input(f"Are you sure you want to delete account for {customers[customer_id]['name']}? (yes/no): ")
            if confirm.lower() == "yes":
                del customers[customer_id]
                transaction.pop(customer_id, None)
                balance.pop(customer_id, None)

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
    

# *****Main Menu*****
while True:
    print("\n ***** ATM MENU *****")
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

        


