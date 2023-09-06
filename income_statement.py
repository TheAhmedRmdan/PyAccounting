"""
This module provides a class `IncomeStatement` to create an income statement.

Classes:
    IncomeStatement: A class to model an income statement.

Imports:
    owner_equity: A module that provides the OwnerEquity class.
    prettytable: A module to create ASCII art tables.
    datetime: A module to work with dates as date objects.
"""

from owner_equity import *
from prettytable import *
import datetime

INCOME_STATEMENT_FILE = "income_statement.txt"


class IncomeStatement:
    """
    A class to represent an income statement.

    ...

    Attributes
    ----------
    issue_date : str
        the date the income statement was created
    income_table : PrettyTable
        a table to display the income statement
    reveneus : list
        a list of all revenue accounts
    reveneus_total_balance : float
        the total balance of all revenue accounts
    expenses : list
        a list of all expense accounts
    expenses_total_balance : float
        the total balance of all expense accounts

    Methods
    -------
    make_row(gacc: list):
        Adds a row to the income statement table for each account in gacc.
    __str__():
        Returns a string representation of the income statement."""

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the income statement object."""

        __class__.income_table.add_row(["Revenues", "", ""])
        __class__.make_row(__class__.reveneus)
        __class__.income_table.add_row(["", "", ""])  # Seperator

        __class__.income_table.add_row(
            ["Total Revenues", "", __class__.reveneus_total_balance], divider=True
        )
        __class__.income_table.add_row(["Expenses", "", ""])
        __class__.make_row(__class__.expenses)

        __class__.income_table.add_row(["", "", ""])  # Seperator
        __class__.income_table.add_row(
            ["Total Expenses", "", __class__.expenses_total_balance], divider=True
        )

        __class__.income_table.add_row(
            [
                "Net Income",
                "",
                (__class__.reveneus_total_balance - __class__.expenses_total_balance),
            ]
        )

        with open(INCOME_STATEMENT_FILE, "w", encoding="utf-8") as is_file:
            is_file.write(str(self))  # Outputting the table

    def __str__(self) -> str:
        return __class__.income_table.get_string()

    issue_date = datetime.datetime.now().strftime("%d %b %Y")

    income_table = PrettyTable(["Income Statement", issue_date, " "])
    income_table.set_style(SINGLE_BORDER)

    reveneus = Revenue.class_childs
    reveneus_total_balance = sum(acc.balance for acc in reveneus)

    expenses = Expense.class_childs
    expenses_total_balance = sum(acc.balance for acc in expenses)

    def make_row(gacc: list):
        """Adds a row to the income statement table for each account in gacc.

        gacc: General Account class_childs list

            gacc stands for General Account [Assets, Liabilities, Owner's Equity]"""

        k = 0
        n = len(gacc)
        gacc_names = [acc.name for acc in gacc]
        while k < n:
            __class__.income_table.add_row(
                [
                    gacc_names[k],
                    gacc[k].balance,
                    "",
                ]
            )
            k += 1
