admin_username="Mathusan"
admin_password="0826"
while True:
        admin_name=input("Enter your Admin user name: ")
        admin_pass=input("enter your Admin password: ")

        if admin_name == admin_username and admin_pass == admin_password:
            print("admin user name and password correct")
            break
        else:
            print("admin user name or password Ronk try agin please")



def show_balance():
    pass


def deposit_money():
    pass

def withdraw_money():
    pass    



while True:
    print("\n *****Bank Menu*****")
    print("1.Register New customer")
    print("2.Create Bank Account")
    print("3.Deposit Money")
    print("4.Withdraw Money")
    print("5.Chake Balance")
    print("6.View Transaction History")
    print("7.View Balance History")  
    print("8.Exit")


    user_select=input("chouse open 1-9:")

    if user_choice=="1":

        register_customer()
    elif user_choice=="2":
        customer_data()
    elif user_choice=="3":
        user_id=int("enter your id:")
        user_pass=int("enter your password:")
        deposit_money()
    elif user_choice=="4":
        withdraw_money()
    elif user_choice=="5":
        check_balance()
    elif user_choice=="6":
        view_transation()
    elif user_choice=="7":
        print("Thanks for using Banking App")
        
    else:
        print("chouse 1 to 9 ")        
                    
        
            
                
