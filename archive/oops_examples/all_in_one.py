from abc import ABC, abstractmethod

class BankAccount:
    bank_name = "Copilot Bank"   # class attribute shared by all accounts

    def __init__(self, owner, balance=0):
        self.owner = owner        # instance attribute
        self._balance = balance   # protected attribute

    # -------------------------------
    # Instance Method
    # -------------------------------
    # Works on a specific object (self).
    def deposit(self, amount):
        self._balance += amount
        print(f"{self.owner} deposited {amount}. Balance: {self._balance}")

    # -------------------------------
    # Class Method
    # -------------------------------
    # Works on the class itself, not a specific object.
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank name changed to {cls.bank_name}")

    # -------------------------------
    # Static Method
    # -------------------------------
    # Utility function: doesn’t depend on class or instance.
    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return True


# -------------------------------
# Abstraction Example
# -------------------------------
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPal(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


# -------------------------------
# Demo
# -------------------------------
if __name__ == "__main__":
    # Instance method demo
    acc1 = BankAccount("Manny", 1000)
    acc1.deposit(500)   # instance method

    # Class method demo
    BankAccount.change_bank_name("Future Bank")  # affects all accounts

    # Static method demo
    try:
        BankAccount.validate_amount(200)  # utility check
        print("Amount is valid")
    except ValueError as e:
        print(e)

    # Abstraction demo
    gateway = PayPal()
    gateway.pay(300)
