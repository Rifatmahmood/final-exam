class Admin:
    def __init__(self, name, email, password, address, bank):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.bank = bank

    def delete_account(self, user):
        found = False
        for account in self.bank.account_list:
            if account.name == user:
                self.bank.account_list.remove(account)
                found = True
                print(f"Account for {user} deleted successfully.")
                break

        if not found:
            print(f"Account with the name '{user}' doesn't exist.")

    def show_users(self):
        for account in self.bank.account_list:
            print(f"Account Name: {account.name}\t Email: {account.email}\t Address: {account.address}\t account type: {account.account_type}")

    def bank_balance(self):
        print(f"{self.bank.name} has {self.bank.balance} taka right now")

    def toggle_loan_feature(self, status):
        self.bank.loan_feature_enabled = status

    def is_bankrupt(self, status):
        self.bank.is_bankrupt = status


