"""
Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: ${self.balance}'

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit accepted and new balance is: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print('Funds Unavailable!')
        else:
            self.balance = self.balance - amount
            print(f"Withdrawal accepted and new balance is: {self.balance}")


acct1 = Account('Jose', 100)
print(acct1)

acct1.deposit(50)
acct1.withdraw(75)
print(acct1.owner)
print(acct1.balance)
acct1.withdraw(500)






