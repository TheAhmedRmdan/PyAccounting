"""
This module contains the Asset class which inherits from the Account class in the account module. 
The Asset class represents an asset account with attributes for name, balance, account type, 
balance sheet, and class children. It also includes methods for initializing the account and 
updating the balance sheet.

Classes:
    Asset(Account): Represents an asset account.
"""
from account import *


class Asset(Account):
    """
    A class to represent an asset account.

    ...

    Attributes
    ----------
    balance_sheet : dict
        a dictionary to store the balance sheet
    class_childs : list
        a list to store the child classes

    Methods
    -------
    __init__(self, name, balance, acc_type="dr"):
        Constructs all the necessary attributes for the asset account object.
    update():
        Updates the balance sheet.
    """

    def __init__(self, name, balance, acc_type="dr"):
        """
        A class to represent an asset account.

        ...

        Attributes
        ----------
        balance_sheet : dict
            a dictionary to store the balance sheet
        class_childs : list
            a list to store the child classes

        Methods
        -------
        __init__(self, name, balance, acc_type="dr"):
            Constructs all the necessary attributes for the asset account object.
        update():
            Updates the balance sheet.
        """

        super().__init__(name, balance, acc_type)

    class_childs = []
