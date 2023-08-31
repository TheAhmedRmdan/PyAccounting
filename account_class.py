"""Small project to model real-world accounting accounts"""
from abc import *


class Account(ABC):
    """A class to model real-world accounting accounts.

    Attributes:
        name (str): The name of the account.
        balance (float or int): The balance of the account.
        acc_type (str): The type of the account. Must be 'dr' or 'cr'"""

    # balance_sheet = {}

    @abstractmethod
    def get_accounts(cls):
        """returns a dict with current accounts"""
        # print(cls.balance_sheet)

    def __str__(self) -> str:
        """Returns a basic account form: Account name, |Balance|, Account Type"""
        return f"{self.name}, |{self.balance}|, {self.acc_type.title()}."

    def __init__(self, name, balance, acc_type: str):
        self.balance = balance
        self.acc_type = acc_type
        self.name = name
        # self.update()

    @property
    def balance(self):
        """balance getter"""
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if not isinstance(new_balance, (int, float)):
            raise ValueError("balance must be int or float")
        self._balance = new_balance

    @property
    def acc_type(self):
        """balance setter"""
        return self._acc_type

    @acc_type.setter
    def acc_type(self, new_type):
        pass
        if new_type not in ["dr", "cr"]:
            raise ValueError("acc_type must be 'dr' or 'cr")
        self._acc_type = new_type

    def debit(self, amount):
        """Debits the account with the specified amount"""
        if self._acc_type == "cr":
            self._balance -= amount
        elif self._acc_type == "dr":
            self._balance += amount
        self.update()

    def credit(self, amount):
        """Credits the account with the specified amount"""
        if self._acc_type == "cr":
            self._balance += amount
        elif self._acc_type == "dr":
            self._balance -= amount
        self.update()  # ! calling an abstract method in a non-abstract method, informative!!!

    @abstractmethod
    def update(self):
        """Updates the balance_sheet dict for every transaction"""
        # Account.balance_sheet[self.name] = self._balance, self._acc_type

    def __add__(self, other):
        """Adding an int or float credits the account balance"""
        self._balance += other
        self.update()
        return self._balance

    def __sub__(self, other):
        self._balance -= other
        self.update()
        return self._balance

    def __truediv__(self, other):
        self._balance /= other
        self.update()
        return self._balance

    def __mul__(self, other):
        self._balance *= other
        self.update()
        return self._balance

    def __eq__(self, other):
        if self._balance == other:
            return True
        else:
            return False


# exp = Account("Expense", 500, "dr")
# rev = Account("Revenue", 800, "cr")
# Account.get_accounts()
# exp + 200
# Account.get_accounts()
# meg = exp.merge(rev, "Merged")
# Account.get_accounts()
# del meg
# Account.get_accounts()
# print(Account.trash)
# print(exp)
