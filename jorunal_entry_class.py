"""Modelling accounting journal"""
import datetime
from account_class import *


JOURNAL_FILE = "journal.txt"


class Entry:
    """A journal entries model"""

    entry_unique_id = 0

    def __init__(self, amount, debit: Account, credit: Account, explaination=""):
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
