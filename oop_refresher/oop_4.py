class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw amount")


account = BankAccount("123456", 1000)

print("Initial balance: ", account.get_balance())
account.set_balance(500)
print("Updated balance: ", account.get_balance())

account.deposit(100)
print("Balance after deposit: ", account.get_balance())
account.withdraw(50)
print("Balance after withdrawal: ", account.get_balance())
