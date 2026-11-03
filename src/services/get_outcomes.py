from src.data_collection.data_maps import DataFrameMap
from src.services.get_winner_picks import get_winner_picks
from streamlit.typing import UploadedFile

def get_outcomes(
    file: UploadedFile,
    winner_picks_url: str | None
) -> DataFrameMap:
    winner_picks_map = get_winner_picks(
        file=file,
        winner_picks_url=winner_picks_url,
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