import pandas as pd
from streamlit.typing import UploadedFile
from src.data_collection.data_maps import DataFrameMap

def scan_nba_team_xpm(
    file: UploadedFile
) -> DataFrameMap:
    xpm_df = pd.read_csv(
        filepath_or_buffer=file,
        header=None
    )

    return DataFrameMap(
        error=None,
        content=xpm_df
    )