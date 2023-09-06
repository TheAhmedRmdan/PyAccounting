"""
This module provides a class `TrialBalance` to create a trial balance.

Classes:
    TrialBalance: A class to model a trial balance.

Imports:
    asset: A module that provides the Asset class.
    liability: A module that provides the Liability class.
    owner_equity: A module that provides the OwnerEquity class.
    prettytable: A module to create ASCII art tables.
"""

from asset import *
from liability import *
from owner_equity import *
from prettytable import *

TRIAL_BALANCE_FILE = "trial_balance.txt"


class TrialBalance:
    """
    A class to represent a trial balance.

    ...

    Attributes
    ----------
    table : PrettyTable
        a table to display the trial balance
    debit_sum_list : list
        a list to keep track of the total debits
    credit_sum_list : list
        a list to keep track of the total credits
    assets : list
        a list of all asset accounts
    assets_names : list
        a list of the names of all asset accounts
    liabs : list
        a list of all liability accounts
    liabs_total_balance : float
        the total balance of all liability accounts
    liabs_names : list
        a list of the names of all liability accounts
    OEs : list
        a list of all owner's equity accounts
    OEs_total_balance : float
        the total balance of all owner's equity accounts
    OEs_names : list
        a list of the names of all owner's equity accounts

    Methods
    -------
    __str__():
        Returns a string representation of the trial balance.
    __repr__():
        Returns a string representation of the trial balance.
    make_row(gacc: list):
        Adds a row to the trial balance table for each account in gacc.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the trial balance object.
        """
        __class__.make_row(__class__.assets)
        __class__.make_row(__class__.liabs)
        __class__.make_row(
            __class__.OEs,
        )
        __class__.table.add_row(["", "", ""], divider=True)
        __class__.table.add_row(
            ["Total", sum(__class__.debit_sum_list), sum(__class__.credit_sum_list)]
        )
        with open(TRIAL_BALANCE_FILE, "w", encoding="utf-8") as trial_bal_file:
            trial_bal_file.write(str(self))

    def __str__(self) -> str:
        return str(__class__.table)

    def __repr__(self) -> str:
        return str(__class__.table)

    table = PrettyTable(["Account", "Debit", "Credit"])
    table.set_style(SINGLE_BORDER)
    debit_sum_list = []
    credit_sum_list = []
    assets = Asset.class_childs

    assets_names = [acc.name for acc in assets]

    liabs = Liab.class_childs
    liabs_total_balance = sum(acc.balance for acc in liabs)
    liabs_names = [acc.name for acc in liabs]

    OEs = OE.class_childs
    OEs_total_balance = sum(acc.balance for acc in OEs)
    OEs_names = [acc.name for acc in OEs]

    def make_row(gacc: list):
        """Adds a row to the trial balance table for each account in gacc.

        gacc: General Account class_childs list

            gacc stands for General Account [Assets, Liabilities, Owner's Equity]
        """

        k = 0
        n = len(gacc)
        gacc_names = [acc.name for acc in gacc]
        while k < n:
            if gacc[k].acc_type == "dr":
                __class__.debit_sum_list.append(gacc[k].balance)
                __class__.table.add_row(
                    [
                        gacc_names[k],
                        gacc[k].balance,
                        "",
                    ]
                )
            else:
                __class__.credit_sum_list.append(gacc[k].balance)
                __class__.table.add_row(
                    [
                        gacc_names[k],
                        "",
                        gacc[k].balance,
                    ]
                )
            k += 1
