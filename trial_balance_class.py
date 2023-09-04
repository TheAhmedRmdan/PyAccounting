from account_class import *
from asset_class import *
from liability_class import *
from OE_classes import *
from prettytable import *


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
        __class__.table.set_style(SINGLE_BORDER)

    def __str__(self) -> str:
        # __class__.table.set_style(MSWORD_FRIENDLY)
        return str(__class__.table)

    def __repr__(self) -> str:
        return str(__class__.table)

    # table = PrettyTable(["Account", "Debit", "Credit"])

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


# make_row(TrialBalance.OEs)
# make_row(TrialBalance.assets)
# make_row(TrialBalance.liabs)
# print(TrialBalance.debit_sum_list)
# print(TrialBalance.credit_sum_list)
# print(bs)
# debit_sum = sum(TrialBalance.debit_sum_list)
# credit_sum = sum(TrialBalance.credit_sum_list)
# x = TrialBalance.make_row
# print(x)
# test = TrialBalance()
# print(test)
