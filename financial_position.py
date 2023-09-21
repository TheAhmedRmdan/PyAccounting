"""
This module provides a class `FinancialPosition` to create a financial position statement.

Classes:
    FinancialPosition: A class to model a financial position statement.

Imports:
    asset: A module that provides the Asset class.
    liability: A module that provides the Liability class.
    owner_equity: A module that provides the OwnerEquity class.
    prettytable: A module to create ASCII art tables.
    datetime: A module to work with dates as date objects.
"""

from asset import *
from liability import *
from owner_equity import *
from prettytable import *
import datetime


FINANCIAL_POSITION_FILE = "Financial_Position.txt"


class FinancialPosition:
    """
    A class to represent a financial position statement.

    ...

    Attributes
    ----------
    assets : list
        a list of all asset accounts
    assets_names : list
        a list of the names of all asset accounts
    assets_total_balance : float
        the total balance of all asset accounts
    issue_date : str
        the date the financial position statement was created
    table : PrettyTable
        a table to display the financial position statement
    liabs : list
        a list of all liability accounts
    liabs_total_balance : float
        the total balance of all liability accounts
    liabs_names : list
        a list of the names of all liability accounts
    OEs : list
        a list of all owner's equity accounts
    capitals : list
        a list of all capital accounts
    reveneus : list
        a list of all revenue accounts
    expenses : list
        a list of all expense accounts
    drawings : list
        a list of all drawing accounts
    OEs_total_balance : float
        the total balance of all owner's equity accounts
    OEs_names : list
        a list of the names of all owner's equity accounts

    Methods
    -------
    make_row(gacc: list):
        Adds a row to the financial position statement table for each account in gacc.
    __str__():
        Returns a string representation of the financial position statement.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the financial position statement object.
        """

        __class__.table.add_row(["Assets", "", ""])
        __class__.make_row(__class__.assets)
        __class__.table.add_row(["Total Assets", "", Asset.acc_sum()], divider=True)

        __class__.table.add_row(
            [
                "Liabilites and Owner's Equity",
                "",
                "",
            ]
        )
        __class__.table.add_row(["Liabilites", "", ""])
        __class__.make_row(__class__.liabs)
        __class__.table.add_row(["Total Liabilites", "", Liab.acc_sum()], divider=True)

        __class__.table.add_row(["Owner's Equity", "", ""])
        __class__.make_row(__class__.OEs)
        __class__.table.add_row(
            ["Total Owner's Equity", "", OE.acc_summing()], divider=True
        )

        __class__.table.add_row(
            [
                "Total Liabilites and Owner's Equity",
                "",
                Liab.acc_sum() + OE.acc_summing(),
            ],
            divider=True,
        )
        __class__.table.add_row(["Date", __class__.issue_date, ""])
        with open(FINANCIAL_POSITION_FILE, "w", encoding="utf-8") as fin_pos_file:
            fin_pos_file.write(str(self))

    issue_date = datetime.datetime.now().strftime("%d %b %Y")
    table = PrettyTable(["Account", "Subtotal", "Total"])
    table.align["Total"] = "r"
    table.set_style(SINGLE_BORDER)

    assets = Asset.class_childs
    assets_names = [acc.name for acc in assets]

    liabs = Liab.class_childs
    liabs_names = [acc.name for acc in liabs]

    OEs = OE.class_childs
    OEs_names = [acc.name for acc in OEs]

    def make_row(gacc: list):
        """Adds a row to the financial position table for each account in gacc.

        gacc: General Account class_childs list

            gacc stands for General Account [Assets, Liabilities, Owner's Equity]"""

        k = 0
        n = len(gacc)
        gacc_names = [acc.name for acc in gacc]
        while k < n:
            __class__.table.add_row(
                [
                    gacc_names[k],
                    gacc[k].balance,
                    "",
                ]
            )
            k += 1

    def __str__(self) -> str:
        return __class__.table.get_string()
