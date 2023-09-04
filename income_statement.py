from OE_classes import *
from prettytable import *
import datetime

INCOME_STATEMENT_FILE = "income_statement.txt"


class IncomeStatement:
    def __init__(self) -> None:
        __class__.income_table.add_row(["Revenues", "", ""])
        __class__.make_row(__class__.reveneus)
        __class__.income_table.add_row(["", "", ""])  # Seperator
        __class__.income_table.add_row(
            ["Total Revenues", "", __class__.reveneus_total_balance], divider=True
        )
        __class__.income_table.add_row(["Expenses", "", ""])
        __class__.make_row(__class__.expenses)
        __class__.income_table.add_row(["", "", ""])
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
            is_file.write(str(self))

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
