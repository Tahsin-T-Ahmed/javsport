import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.get_soup import get_soup
from src.services.get_win_trends import get_win_trends
from streamlit.typing import UploadedFile

def process_outcomes(
    file: UploadedFile,
    winner_picks_url: str | None
) -> DataFrameMap:
    file_raw = pd.read_csv(file)

    if "WINNER RECORD" not in file_raw.columns:
        return DataFrameMap(
            error=f"ERROR (Outcomes-Processor): 'WINNER RECORD' column not found",
            content=None
        )

    return DataFrameMap(
        error=None,
        content=file_raw
    )