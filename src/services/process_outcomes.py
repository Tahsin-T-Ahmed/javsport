import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.get_soup import get_soup
from src.services.get_win_trends import get_win_trends
from streamlit.typing import UploadedFile

def process_outcomes(
    file: UploadedFile,
    win_trends_url: str
) -> DataFrameMap:
    file_raw = pd.read_csv(file)

    if "WINNER RECORD" not in file_raw.columns:
        return DataFrameMap(
            error=f"ERROR (Outcomes-Processor): 'WINNER RECORD' column not found",
            content=None
        )

    wintrends_map = get_win_trends(
        url=win_trends_url
    )

    if wintrends_map["error"]:
        return DataFrameMap(
            error=wintrends_map["error"],
            content=None
        )

    win_trends = wintrends_map["content"]

    return DataFrameMap(
        error=None,
        content=file_raw
    )