#  Encapsulation hides sensitive data using private (__) and protected (_) attributes

class BankAccount:
    def __init__(self, balance):
        self._protected_balance = balance  # Protected attribute
        self.__private_balance = balance   # Private attribute

    def get_private_balance(self):
        return self.__private_balance

# Usage
account = BankAccount(1000)
print(account._protected_balance)  # Output: 1000 (Accessible but should be used cautiously)
print(account.get_private_balance())  # Output: 1000 (Accessing private attribute via method)