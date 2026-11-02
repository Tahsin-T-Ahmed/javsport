import pandas as pd
from src.data_collection.builders.make_winner_picks import make_winner_picks
from src.data_collection.data_maps import DataFrameMap
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

    winner_picks = None

    if winner_picks_url:
        winner_picks_map = make_winner_picks(
            url=winner_picks_url
        )

        if winner_picks_map["error"]:
            return DataFrameMap(
                error=winner_picks_map["error"],
                content=None
            )

        winner_picks = winner_picks_map["content"]

    return DataFrameMap(
        error=None,
        content=file_raw
    )