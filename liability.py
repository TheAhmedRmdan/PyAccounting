"""
This module contains the Liab class which inherits from the Account class in the account module. 
The Liab class represents a liability account with attributes for name, balance, account type, 
balance sheet, and class children. It also includes methods for initializing the account and 
updating the balance sheet.

Classes:
    Liab(Account): Represents a liability account.
"""
from account import Account


class Liab(Account):
    """
    A class to represent a liability account.

    ...

    Attributes
    ----------
    balance_sheet : dict
        a dictionary to store the balance sheet
    class_childs : list
        a list to store the child classes

    Methods
    -------
    __init__(self, name, balance, acc_type="cr"):
        Constructs all the necessary attributes for the liability account object.
    update():
        Updates the balance sheet."""

    def __init__(self, name, balance, acc_type="cr"):
        """
        Constructs all the necessary attributes for the liability account object.

        Parameters
        ----------
            name : str
                the name of the account
            balance : float
                the balance of the account
            acc_type : str, optional
                the type of the account (default is "cr")
        """
        super().__init__(name, balance, acc_type)
        __class__.class_childs.append(self)
        self.update()

    balance_sheet = {}
    class_childs = []
