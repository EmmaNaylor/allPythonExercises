from insufficient_funds import InsufficientFundsException

class Account:

    def __init__(self, funds):
        self._balance = funds

    def check_balance(self):
        try:
            check_bal_test = self._balance / 2
        except TypeError as exc:
            print("Oops! This script takes only numbers! check_balance() failed!\n"
                  "Error captured as:", exc)
        else:
            print(f"Your balance is: £{self._balance}")
            return self._balance

    def deposit(self, amount):
        try:
            self._balance += amount
        except TypeError as exc:
            print("Oops! This script takes only numbers! Deposit() failed!\n"
                  "Error captured as:", exc)

    def withdraw(self, amount):
        try:
            self._balance -= amount
        except TypeError as exc:
            print("Oops! This script takes only numbers! withdraw() failed!\n"
                  "Error captured as:", exc)
        else:
            if self._balance < 0:
                self._balance += amount
                raise InsufficientFundsException(f"You tried to withdraw £{amount} but you have insufficient funds to withdraw that amount")



