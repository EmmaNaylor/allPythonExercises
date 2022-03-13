from standard_account import Account
from savings import Savings

print("*********Standard Account*********")
my_account = Account(20)
my_account.check_balance()
my_account.deposit(80)
my_account.check_balance()
my_account.withdraw(10)
my_account.check_balance()
my_account.withdraw(1000)
my_account.check_balance()

print("*********Savings Account*********")
save = Savings(20, 2)
save.check_balance()
save.deposit(2000)
save.deposit(4000)
save.check_balance()
save.calc_interest()
