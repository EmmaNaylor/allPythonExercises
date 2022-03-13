class InsufficientFundsException(Exception):
    pass


class Account:

    def __init__(self, funds):
        self._balance = funds

    def check_balance(self):
        print(f"Your balance is: £{self._balance}")
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        try:
            self._balance -= amount
            if self._balance < 0:
                self._balance += amount
                raise InsufficientFundsException("You have insufficient funds to withdraw that amount")
        except InsufficientFundsException as err:
            print("Oops:", err)


