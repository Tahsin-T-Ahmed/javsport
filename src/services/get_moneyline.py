import datetime
import numpy as np
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers.scan_odds_table import scan_odds_table
from src.utils.convert_moneyline import convert_moneyline
from streamlit.typing import UploadedFile

def get_moneyline(
    file: UploadedFile,
    timestamp: datetime.datetime
) -> DataFrameMap:
    odds_map = scan_odds_table(
        file=file,
        timestamp=timestamp
    )

    if odds_map["error"]:
        return DataFrameMap(
            error=odds_map["error"],
            content=None
        )

    moneyline_df = odds_map["content"]

    if "MONEY LINE" not in moneyline_df.columns:
        return DataFrameMap(
            error=f"ERROR (Moneyline-Retriever): No column named 'MONEY LINE' found",
            content=None
        )

    moneyline_df["MONEY LINE"] = moneyline_df["MONEY LINE"].astype(float)

    moneyline_df["PROBABILITY"] = moneyline_df["MONEY LINE"].apply(
        func=convert_moneyline
    )

    return DataFrameMap(
        error=None,
        content=moneyline_df
    )