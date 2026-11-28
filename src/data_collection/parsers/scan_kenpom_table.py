import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from streamlit.typing import UploadedFile

def scan_kenpom_table(
    file: UploadedFile
) -> DataFrameMap:
    kenpom_df = pd.read_csv(
        filepath_or_buffer=file,
        header=None
    )

    kenpom_df = kenpom_df.loc[
        2:,
        [0, 3, 8]
    ]

    kenpom_df.columns = ["TEAM KENPOM NAME", "OFFENSIVE RATING", "DEFENSIVE RATING"]

    kenpom_df.reset_index(drop=True, inplace=True)

    return DataFrameMap(
        error=None,
        content=kenpom_df
    )