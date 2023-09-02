from account_class import Account


class Asset(Account):
    """Assets account model"""

    balance_sheet = {}

    def __init__(self, name, balance, acc_type="dr"):
        super().__init__(name, balance, acc_type)
        self.update()
