"""This module provides a class `TrialBalance` to create an accounting trial balance."""


from asset import *
from liability import *
from owner_equity import *
from prettytable import *

TRIAL_BALANCE_FILE = "trial_balance.txt"


class TrialBalance:
    def __init__(self) -> None:
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
