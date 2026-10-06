
# Python OOP - Encapsulation

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful:", amount)
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def show_balance(self):
        print("Account holder:", self.owner)
        print("Balance:", self.__balance)


account = BankAccount("Mohammed", 1000)

account.show_balance()

account.deposit(500)
account.withdraw(200)

account.show_balance()