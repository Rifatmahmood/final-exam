from datetime import datetime


class Bank:
    def __init__(self, name):
        self.name = name
        self.account_list = []
        self.admin_list = []
        self.balance = 1000000000
        self.loan_amount = 0
        self.loan_feature_enabled = True
        self.is_bankrupt = False

    def add_account(self, user):
        self.account_list.append(user)

    def add_admin_account(self, admin):
        self.admin_list.append(admin)

    def __str__(self):
        return f"Bank Name {self.name} with accounts : {len(self.account_list)}"


class User:
    def __init__(self, name, email, password, address,  account_type, bank):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.account_type = account_type
        self.account_num = f"{self.name}{'10' + str(len(bank.account_list))}"
        self.balance = 0
        self.loan_taken = 0
        self.transaction_history = []
        self.bank = bank

    def check_balance(self):
        print(f"{self.balance}")

    def deposit(self, amount):
        transaction_type = "deposit"
        self.balance += amount
        transaction_details = TransactionDetails(self,transaction_type, amount)
        self.transaction_history.append(transaction_details)

    def withdraw(self, amount):
        if self.bank.is_bankrupt is False:
            if self.balance >= amount:
                transaction_type = "withdraw"
                if amount > self.balance:
                    print("Withdrawal amount exceeded")
                else:
                    self.balance -= amount
                transaction_details = TransactionDetails(self, transaction_type, amount)
                self.transaction_history.append(transaction_details)
        else:
            print(f"{self.bank.name} is now bankrupt")

    def transfer(self, send_to_user, amount):
        transaction_type = "transfer"
        if self.bank.is_bankrupt is False:
            if self.balance > amount:
                if send_to_user in self.bank.account_list:
                    send_to_user.balance += amount
                    self.balance -= amount
                    transaction_details = TransactionDetails(self, transaction_type, amount)
                    self.transaction_history.append(transaction_details)
                else:
                    print("Account does not exist")
            else:
                print("Inefficient Balance")
        else:
            print(f"{self.bank.name} is now bankrupt")

    def take_loan(self, amount):
        transaction_type = "loan"
        if self.bank.loan_feature_enabled:
            if self.loan_taken < 2:
                if self.bank.balance > amount:
                    self.balance += amount
                    self.bank.balance -= amount
                    self.bank.loan_amount += amount
                    self.loan_taken += 1
                    transaction_details = TransactionDetails(self, transaction_type, amount)
                    self.transaction_history.append(transaction_details)
                else:
                    print("Pls, Come back tomorrow, server is down")
            else:
                print("You can't Take loan more than twice")
        else:
            print("Loaning is off right now")

    def show_transactional_history(self):

        print(f"\n{self.name}'transaction history ")
        print("=============================")
        for trans in self.transaction_history:
            print(f"The {trans.transaction_type} transaction wih ID : {trans.transaction_id} \nhappened in {trans.transaction_time}")
            print(F"The {trans.transaction_type} was {trans.amount}")
            print(f"{trans.user_name}'s balance is {trans.user_balance}")
            print("-----------------------------")


class TransactionDetails:

    def __init__(self, user, transaction_type, amount ):
        self.transaction_id = f"{"10000" + str(len(user.transaction_history))}"
        self.transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_type = transaction_type.capitalize()
        self.amount = amount
        self.user_balance = user.balance
        self.user_name = user.name






