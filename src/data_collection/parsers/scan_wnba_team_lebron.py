import pandas as pd
from streamlit.typing import UploadedFile
from src.data_collection.data_maps import DataFrameMap

def scan_wnba_team_lebron(
    file: UploadedFile
) -> DataFrameMap:
    lebron_df = pd.read_csv(
        filepath_or_buffer=file,
        header=None
    )

    return DataFrameMap(
        error=None,
        content=lebron_df
    )