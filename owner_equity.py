"""Owner's Equity accouts models"""
from account import Account


class OE(Account):
    """Owner's Equity accout model"""

    def __init__(self, name, balance, acc_type="cr"):
        super().__init__(name, balance, acc_type)

    class_childs = []

    def update(self):
        """Sepcial implementation for the OE class only.
        Updates the class childs list for every transaction"""
        self.__class__.class_childs.append(self)
        __class__.class_childs.append(self)

    @classmethod
    def acc_summing(cls):
        """Special implementation for a special account"""
        return (
            Capital.acc_sum()
            + Revenue.acc_sum()
            - Expense.acc_sum()
            - Drawing.acc_sum()
        )


class Capital(OE):
    """Owner's Capital accout model"""

    def __init__(self, name, balance, acc_type="cr"):
        super().__init__(name, balance, acc_type)

    class_childs = []


class Revenue(OE):
    """Revenues accout model"""

    def __init__(self, name, balance, acc_type="cr"):
        super().__init__(name, balance, acc_type)

    class_childs = []


class Expense(OE):
    """Expenses accout model"""

    def __init__(self, name, balance, acc_type="dr"):
        super().__init__(name, balance, acc_type)

    balance_sheet = {}
    class_childs = []


class Drawing(OE):
    """Owner's drawings accout model"""

    def __init__(self, name, balance, acc_type="dr"):
        super().__init__(name, balance, acc_type)

    class_childs = []
