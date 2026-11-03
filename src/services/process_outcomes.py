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
    
    winner_picks_url_adjusted = f"{winner_picks_url}?range=last-21-days"

    winner_picks_map = get_outcomes(
        file=file,
        winner_picks_url=winner_picks_url_adjusted,
        month=month,
        day=day
    )

    if winner_picks_map["error"]:
        return DataFrameMap(
            error=winner_picks_map["error"],
            content=None
        )

    winner_picks = winner_picks_map["content"]

    return DataFrameMap(
        error=None,
        content=winner_picks
    )