import io
import pandas as pd

def parse_text(moneyline_text:str) -> pd.DataFrame:
    moneyline_input = io.StringIO(moneyline_text)

    moneyline_table = pd.read_json(moneyline_input)

    return moneyline_table