"""Liabilites accounts model"""
from account_class import Account


class Liab(Account):
    """Liabilites accounts model"""

    def __init__(self, name, balance, acc_type="cr"):
        super().__init__(name, balance, acc_type)

    balance_sheet = {}
