import io
import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def parse_text(moneyline_text: str) -> DataFrameMap:
    moneyline_input = io.StringIO(moneyline_text)

    moneyline_table = pd.read_json(moneyline_input)

    return dict(
        error = None,
        content = moneyline_table
    )