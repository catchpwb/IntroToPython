# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:50:56 2025

@author: Will
"""
"""
page 325
Develop a class BankAccount that supports these methods:
• __init__(): Initializes the bank account balance to the value of the input argument,
or to 0 if no input argument is given
• withdraw(): Takes an amount as input and withdraws it from the balance
• deposit(): Takes an amount as input and adds it to the balance
• balance(): Returns the balance on the account
>>> x = BankAccount(700)
>>> x.balance())
700.00
>>> x.withdraw(70)
>>> x.balance()
630.00
>>> x.deposit(7)
>>> x.balance()
637.00
"""

class BankAccount:
    'represents a bank account with withdraw, deposit, balance methods'

    def __init__(self, initial = 0):
        'initialize balance'
        self.initial = initial

    def withdraw(self, takeOut):
        'withdraw from account'
        self.initial -= takeOut

    def deposit(self, putIn):
        'deposit money into account'
        self.initial += putIn

    def balance(self):
        'check remaining balance'
        print(self.initial)


x = BankAccount(700)
x.balance()
x.withdraw(70)
x.balance()
x.deposit(7)
x.balance()
help(BankAccount)
