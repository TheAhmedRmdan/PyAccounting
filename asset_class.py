"""Assets accounts model"""
from account_class import *


class Asset(Account):
    """Assets accounts model"""

    def __init__(self, name, balance, acc_type="dr"):
        super().__init__(name, balance, acc_type)
        __class__.class_childs.append(self)
        self.update()

    balance_sheet = {}
    class_childs = []
