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


cash = Asset("cash", 500)
cash.debit(100)
exp = Asset("expense", 200, "dr")

# print(cash.balance)
# x = Asset.class_childs
# total_balance = sum(acc.balance for acc in Asset.class_childs)
# names = [acc.name for acc in Asset.class_childs]
# print(names)
# print(total_balance)
