from admin import Admin
from user import User, Bank

world_bank = Bank("Islam Bank")

rifat = User("rifat", "rft@gmail.com", 5656, "dhaka", "crr", world_bank)
world_bank.add_account(rifat)
rifat.deposit(5000)

raihan = User("raihan", "rft@gmail.com", 6767, "dhaka", "crr", world_bank)
world_bank.add_account(raihan)
raihan.deposit(8000)


def find_account(name, password):
    for account in world_bank.account_list:
        if account.name == name and account.password == password:
            return account
        else:
            print(f"You don't have any account with this {name}")
    return None


def find_admin(name, password):
    for admin in world_bank.admin_list:
        if admin.name == name and admin.password == password:
            return admin
        else:
            print(f"You don't have any account with this {name}")
    return None


def user_menu():
    while True:
        print("Welcome!!")
        print("0. Create Account")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Take Loan")
        print("6. Show Transactional History")
        print("7. Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 0:
            print("To create your account give this info")
            name = input("Enter Your Name: ")
            email = input("Enter Your Email: ")
            password = input("Enter Your Password: ")
            address = input("Enter Your Address: ")
            account_type = input("Which type of account would you want? current or savings?: ")
            account_holder = User(name, email, password, address, account_type, world_bank)
            world_bank.add_account(account_holder)
            print("User Account Created Successfully")

        elif choice == 1:
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_account = find_account(name, password)
            if found_account:
                amount = int(input("Enter the amount you want to deposit: "))
                found_account.deposit(amount)
                print(f"${amount} deposited successfully.")
            else:
                print("Create Account First")

        elif choice == 2:
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_account = find_account(name, password)
            if found_account:
                amount = int(input("Enter the amount you want to withdraw: "))
                found_account.withdraw(amount)
            else:
                print("Create Account First")

        elif choice == 3:
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_account = find_account(name, password)
            if found_account:
                found_account.check_balance()
            else:
                print("Create Account First")

        elif choice == 4:
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_account = find_account(name, password)
            recipient_name = input("Enter the name of the recipient: ")
            amount = int(input(f"Enter the amount you want to transfer to {recipient_name}"))
            found_account.transfer(recipient_name, amount)

        elif choice == 5:
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_account = find_account(name, password)
            if found_account:
                loan_amount = int(input("Enter the amount you want to borrow: "))
                found_account.take_loan(loan_amount)
            else:
                print("Create Account First")

        elif choice == 6:
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_account = find_account(name, password)
            if found_account:
                found_account.show_transactional_history()
            else:
                print("Create Account First")

        elif choice == 7:
            print("Exiting the menu...")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 7.")


def admin_menu():
    while True:
        print("Admin Menu:")
        print("0. Create Admin Account")
        print("1. Show Users")
        print("2. Delete Account")
        print("3. View Bank Balance")
        print("4. Toggle Loan Feature")
        print("5. Check Bankruptcy Status")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "0":
            print("To create your account give this info")
            name = input("Enter Your Name: ")
            email = input("Enter Your Email: ")
            password = input("Enter Your Password: ")
            address = input("Enter Your Address: ")
            admin_account = Admin(name, email, password, address, world_bank)
            world_bank.add_admin_account(admin_account)
            print("Admin Account Created Successfully")

        elif choice == "1":
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_admin = find_admin(name, password)
            if found_admin:
                found_admin.show_users()
            else:
                print("Create Account First")

        elif choice == "2":
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_admin = find_admin(name, password)
            if found_admin:
                name = input("Enter the name of the account holder to delete: ")
                found_admin.delete_account(name)
            else:
                print("Create Account First")

        elif choice == "3":
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_admin = find_admin(name, password)
            if found_admin:
                found_admin.bank_balance()
            else:
                print("Create Account First")

        elif choice == "4":
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_admin = find_admin(name, password)
            if found_admin:
                status = input("Enter 'enable' to enable or 'disable' to disable the loan feature: ").lower()
                if status == "enable":
                    found_admin.toggle_loan_feature(True)
                    print("Loan feature enabled.")
                elif status == "disable":
                    found_admin.toggle_loan_feature(False)
                    print("Loan feature disabled.")
                else:
                    print("Invalid input. Please enter 'enable' or 'disable'.")

        elif choice == "5":
            name = input("Enter Your Name: ")
            password = input("Enter Your Password: ")
            found_admin = find_admin(name, password)
            if found_admin:
                status = input("Enter 'bankrupt' to enable or 'not bankrupt' to disable the loan feature: ").lower()
                if status == "bankrupt":
                    found_admin.is_bankrupt(True)
                    print("Bank is bankrupt")
                elif status == "not bankrupt":
                    found_admin.is_bankrupt(False)
                    print("Bank is not bankrupt")
                else:
                    print("Invalid input. Please enter 'bankrupt' or 'not bankrupt'.")

        elif choice == "6":
            print("Exiting admin menu...")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 6.")


while True:
    print(f"Welcome!! to {world_bank.name}")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        user_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        print("Exiting Main menu...")
        break
    else:
        print("Invalid Input!!")
