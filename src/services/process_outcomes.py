import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.services.get_outcomes import get_outcomes
from streamlit.typing import UploadedFile

def process_outcomes(
    file: UploadedFile,
    month: int | str,
    day: int | str,
    winner_picks_url: str | None
) -> DataFrameMap:
    file_raw = pd.read_csv(file)

    winner_picks = get_outcomes(
        winner_picks_url=winner_picks_url,
        month=month,
        day=day
    )

    return DataFrameMap(
        error=None,
        content=file_raw
    )