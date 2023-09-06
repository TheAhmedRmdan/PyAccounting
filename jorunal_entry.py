"""
This module models an accounting journal. It provides a class `Entry` to create journal entries and manage them in a journal file.

Classes:
    Entry: A class to model a journal entry.

Imports:
    datetime: A module to work with dates as date objects.
    account: A module that provides the Account class.
"""
import datetime
from account import *


JOURNAL_FILE = "journal.txt"


class Entry:
    """
    A class to represent a journal entry.

    ...

    Attributes
    ----------
    entry_unique_id : int
        a class attribute to keep track of the number of entries created
    id : int
        a unique identifier for each entry
    amount : int or float
        the amount of the entry
    debit_side : Account
        the account to be debited
    credit_side : Account
        the account to be credited
    explain : str
        a brief explanation of the entry
    date : str
        the date the entry was created

    Methods
    -------
    __str__():
        Returns a string representation of the entry.
    amount():
        Property getter for the amount attribute.
    amount(new_amount):
        Property setter for the amount attribute.
    debit_side():
        Property getter for the debit_side attribute.
    debit_side(other):
        Property setter for the debit_side attribute.
    credit_side():
        Property getter for the credit_side attribute.
    credit_side(other):
        Property setter for the credit_side attribute.
    __del__():
        Deletes the entry from the journal file when the entry object is deleted.
    """

    entry_unique_id = 0

    def __init__(self, amount, debit: Account, credit: Account, explaination=""):
        """
        A class to represent a journal entry.

        ...

        Attributes
        ----------
        entry_unique_id : int
            a class attribute to keep track of the number of entries created
        id : int
            a unique identifier for each entry
        amount : int or float
            the amount of the entry
        debit_side : Account
            the account to be debited
        credit_side : Account
            the account to be credited
        explain : str
            a brief explanation of the entry
        date : str
            the date the entry was created

        Methods
        -------
        __str__():
            Returns a string representation of the entry.
        amount():
            Property getter for the amount attribute.
        amount(new_amount):
            Property setter for the amount attribute.
        debit_side():
            Property getter for the debit_side attribute.
        debit_side(other):
            Property setter for the debit_side attribute.
        credit_side():
            Property getter for the credit_side attribute.
        credit_side(other):
            Property setter for the credit_side attribute.
        __del__():
            Deletes the entry from the journal file when the entry object is deleted."""

        __class__.entry_unique_id += 1
        self.id = __class__.entry_unique_id
        self.amount = amount
        self.debit_side = debit
        self.credit_side = credit
        self.explain = explaination
        self.date = datetime.datetime.now().strftime("%d %b %Y")
        self.debit_side.debit(amount)
        self.credit_side.credit(amount)

        with open(JOURNAL_FILE, "r+") as j_file:
            contents = j_file.read()
            if str(self) in contents:
                print(f"This entry {str(self)} already exists in the Journal")
                duplicate_choice_msg = (
                    "\nDo you want to add it again as a duplicate [Y] or no? [n]: "
                )
                duplicate_choice = input(duplicate_choice_msg).lower()
                if duplicate_choice == "y":
                    j_file.write(f"{str(self)}\n")
                else:
                    pass

            else:
                j_file.write(f"{str(self)}\n")

    def __str__(self) -> str:
        return str(
            {
                "Date": self.date,
                "Explaination": self.explain,
                "Amount": self.amount,
                "Debit": self.debit_side.name,
                "Credit": self.credit_side.name,
            }
        )

    @property
    def amount(self):
        """amount getter"""
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if not isinstance(new_amount, (int, float)):
            raise ValueError("balance must be int or float")
        self._amount = new_amount

    @property
    def debit_side(self):
        return self._debit_side

    @debit_side.setter
    def debit_side(self, other):
        if not isinstance(other, Account):
            raise ValueError("Debit side must be an Account object")
        self._debit_side = other

    @property
    def credit_side(self):
        return self._credit_side

    @credit_side.setter
    def credit_side(self, other):
        if not isinstance(other, Account):
            raise ValueError("Credit side must be an Account object")
        self._credit_side = other

    def __del__(self):
        try:
            with open(JOURNAL_FILE, "r") as j_file:
                contents = j_file.read()

            delete_text = contents.replace(str(self), "")

            with open(JOURNAL_FILE, "w") as j_file:
                j_file.write(delete_text)
        except NameError:
            pass
