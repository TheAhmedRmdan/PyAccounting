from asset_class import *
from liability_class import *
from OE_classes import *
from prettytable import *
import datetime

FINANCIAL_POSITION_FILE = "Financial_Position.txt"


class FinancialPosition:
    def __init__(self) -> None:
        __class__.table.add_row(["Assets", "", ""])
        __class__.make_row(__class__.assets)
        __class__.table.add_row(
            ["Total Assets", "", __class__.assets_total_balance], divider=True
        )
        __class__.table.add_row(
            [
                "Liabilites and Owner's Equity",
                "",
                "",
            ]
        )
        __class__.table.add_row(["Liabilites", "", ""])
        __class__.make_row(__class__.liabs)
        __class__.table.add_row(
            ["Total Liabilites", "", __class__.liabs_total_balance], divider=True
        )
        __class__.table.add_row(["Owner's Equity", "", ""])
        __class__.make_row(__class__.OEs)
        __class__.table.add_row(
            ["Total Owner's Equity", "", __class__.OEs_total_balance], divider=True
        )
        __class__.table.add_row(
            [
                "Total Liabilites and Owner's Equity",
                "",
                __class__.liabs_total_balance + __class__.OEs_total_balance,
            ],
            divider=True,
        )
        __class__.table.add_row(["Date", __class__.issue_date, ""])
        with open(FINANCIAL_POSITION_FILE, "w", encoding="utf-8") as fin_pos_file:
            fin_pos_file.write(str(self))

    assets = Asset.class_childs
    assets_names = [acc.name for acc in assets]
    assets_total_balance = sum(acc.balance for acc in assets)
    issue_date = datetime.datetime.now().strftime("%d %b %Y")
    table = PrettyTable(["Account", "Subtotal", "Total"])
    table.align["Total"] = "r"
    table.set_style(SINGLE_BORDER)
    liabs = Liab.class_childs
    liabs_total_balance = sum(acc.balance for acc in liabs)
    liabs_names = [acc.name for acc in liabs]

    OEs = OE.class_childs
    capitals = Capital.class_childs
    reveneus = Revenue.class_childs
    expenses = Expense.class_childs
    drawings = Drawing.class_childs
    OEs_total_balance = (
        sum(acc.balance for acc in capitals)
        + sum(acc.balance for acc in reveneus)
        - sum(acc.balance for acc in expenses)
        - sum(acc.balance for acc in drawings)
    )

    OEs_names = [acc.name for acc in OEs]

    def make_row(gacc: list):
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
