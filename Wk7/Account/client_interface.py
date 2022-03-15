from standard_account import Account
from savings import Savings
from insufficient_funds import InsufficientFundsException

print("*********Standard Account*********")
my_account = Account(20)  # should return 20
my_account.check_balance()

my_account.deposit(80)
my_account.check_balance()  # should return 100

try:
    my_account.withdraw(20)
except InsufficientFundsException as err:
    print("Oops:", err)

try:
    my_account.withdraw(20)
except InsufficientFundsException as err:
    print("Oops:", err)

my_account.check_balance()  # should return 60

try:
    my_account.withdraw(1000)
except InsufficientFundsException as err:
    print("Oops:", err)

my_account.check_balance()

print("*********Savings Account*********")
save = Savings(20, 2)
save.check_balance()
save.deposit(2000)
save.deposit(4000)
save.check_balance()
save.withdraw(200)
save.check_balance()
save.calc_interest()
