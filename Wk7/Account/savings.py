from standard_account import Account


class Savings(Account):
    standard_rate = 0.025 # per annum

    def __init__(self, funds, years):
        Account.__init__(self, funds)
        self._balance = funds
        self.years = years

    def calc_interest(self):
        final_rate = self.years * self.standard_rate
        interest = round(final_rate * self._balance)
        print(f"With a balance of £{self._balance} over {self.years} years. You will accrue £{interest} in interest")

