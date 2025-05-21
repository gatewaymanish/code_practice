# Hides sensitive data using private attributes (__balance).


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500