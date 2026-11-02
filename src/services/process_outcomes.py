import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.services.get_outcomes import get_outcomes
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

    winner_picks = get_outcomes(
        winner_picks_url=winner_picks_url
    )

    return DataFrameMap(
        error=None,
        content=file_raw
    )