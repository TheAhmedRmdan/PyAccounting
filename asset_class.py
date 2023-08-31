from account_class import *


class Asset(Account):
    """Assets account model"""

    assets_dict = {}

    def __init__(self, name, balance, acc_type: str):
        super().__init__(name, balance, acc_type)
        self.update()

    @classmethod
    def get_accounts(cls):
        """returns a dict with current accounts"""
        print(cls.assets_dict)

    def update(self):
        """Updates the assets_dict for every transaction"""
        Asset.assets_dict[self.name] = self._balance, self._acc_type


cash = Asset("Cash", 2500, "dr")
gold = Asset("Gold", 1800, "dr")

x = gold == 1800
print(x)
