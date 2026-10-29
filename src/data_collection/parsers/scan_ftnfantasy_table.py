import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from streamlit.typing import UploadedFile

def scan_ftnfantasy_table(
    file: UploadedFile
) -> DataFrameMap:
    table = pd.read_csv(file)

    return DataFrameMap(
        error=None,
        content=table
    )