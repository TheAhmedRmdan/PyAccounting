"""Assets accounts model"""
from account_class import Account


class Asset(Account):
    """Assets accounts model"""

    def __init__(self, name, balance, acc_type="dr"):
        super().__init__(name, balance, acc_type)
        self.update()

    balance_sheet = {}


# cash = Asset("cash", 500)
# exp = Account("expense", 200, "dr")
