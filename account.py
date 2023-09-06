"""
This module provides a representation of an accounting account. It includes a class, Account, which models the behavior of an accounting account in a double-entry bookkeeping system. The Account class supports operations such as debiting and crediting amounts, updating the account balance, and performing arithmetic operations on the account balance.

Class:
Account: Models an accounting account with attributes for the account name, balance, and type (debit or credit). Supports operations for debiting and crediting amounts, updating the account balance, and performing arithmetic operations on the account balance.
"""


class Account:
    """
    A class to represent an accounting account in a double-entry bookkeeping system.

    ...

    Attributes
    ----------
    name : str
        the name of the account
    balance : int or float
        the balance of the account
    acc_type : str
        the type of the account, either 'dr' (debit) or 'cr' (credit)

    Methods
    -------
    get_accounts():
        Class method that prints a dictionary of all current accounts.
    debit(amount):
        Debits the account with a specified amount.
    credit(amount):
        Credits the account with a specified amount.
    update():
        Updates the balance_sheet dictionary for every transaction.
    __add__(other):
        Adds an integer or float to the account balance.
    __sub__(other):
        Subtracts an integer or float from the account balance.
    __truediv__(other):
        Divides the account balance by an integer or float.
    __mul__(other):
        Multiplies the account balance by an integer or float.
    __eq__(other):
        Checks if the account balance is equal to a specified value.
    __repr__():
        Returns a tuple representation of the Account instance."""

    def __init__(self, name, balance, acc_type):
        """
        Constructs all the necessary attributes for the Account object.

        Parameters:
            name (str): The name of the account.
            balance (int or float): The initial balance of the account.
            acc_type (str): The type of the account, either 'dr' (debit) or 'cr' (credit).
        """
        self.balance = balance
        self.acc_type = acc_type
        self.name = name
        self.update()

    def __str__(self) -> str:
        """Returns a basic account form: Account name, |Balance|, Account Type"""
        return f"{self.name}, |{self.balance}|, {self.acc_type.title()}."

    balance_sheet = {}

    @classmethod
    def get_accounts(cls):
        """returns a dict with current accounts"""
        print(cls.balance_sheet)

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

    def update(self):  # previously @abstractmetohd
        # TODO updating the bs dict is unnecessary, change it to update the class childs
        # TODO instead of doing it in every init
        """Updates the balance_sheet dict for every transaction"""
        self.__class__.balance_sheet[self.name] = self._balance, self._acc_type

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

    def __repr__(self):
        return f"{tuple([self.name,self.balance,self.acc_type])}"
