# account.py
'''
script: cis131_assignment_Account_Class_Read_only
action: A test class for a bank account, it keeps track of the balance and allows deposites.
Author: Declan Juliano
Date:   9/29/2025
'''

"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self._name = name
        self._balance = balance
        
    #return the name but dont allow it to be changed
    @property
    def name(self):
        return self._name
    
    #return the balance but dont allow it to be changed
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self._balance += amount

# make acc an account
acc=Account('John',Decimal('0.04'))

#deposit to acc
acc.deposit(Decimal('200'))
print(acc.balance)

#attempt to change the balance, 
try:
    acc.balance=99999
except Exception as e:
    print("that is not how that works ",e)
    print("the remaining balance is ", acc.balance)

try:
    acc.name = 'Mark'
except Exception as e:
    print("that is not how that works ",e)
    print("The name is ",acc.name)

#deposit to acc
acc.deposit(Decimal(100))
print(acc.balance)