"""Assets accounts model"""
from account import *


class Asset(Account):
    """Assets accounts model
    instantiation arguments are the same for all accounts (same as base class Account).
    """

    def __init__(self, name, balance, acc_type="dr"):
        super().__init__(name, balance, acc_type)
        __class__.class_childs.append(self)
        self.update()

    balance_sheet = {}
    class_childs = []
