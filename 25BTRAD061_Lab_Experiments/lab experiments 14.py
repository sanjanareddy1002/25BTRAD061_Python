class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance: Rs.", self.__balance)


account = BankAccount("Dharani", 5000)

account.check_balance()
account.deposit(2000)
account.withdraw(1000)
account.withdraw(10000)
account.deposit(-500)
account.check_balance()
