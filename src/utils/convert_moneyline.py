import numpy as np

def convert_moneyline(
    moneyline: float
):
    if moneyline > 0:
        return (
            100 / (moneyline + 100)
        )

    moneyline_abs_val = np.abs(moneyline)

    return (
        moneyline_abs_val / (moneyline_abs_val + 100)
    )