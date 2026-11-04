from src.data_collection.data_maps import DataFrameMap
from src.services.get_winners import get_winners
from streamlit.typing import UploadedFile

def get_outcomes(
    file: UploadedFile,
    winner_picks_url: str | None
) -> DataFrameMap:
    winners_map = get_winners(
        file=file,
        winner_picks_url=winner_picks_url
    )

    if winners_map["error"]:
        return DataFrameMap(
            error=winners_map["error"],
            content=None
        )

    winners = winners_map["content"]

    return DataFrameMap(
        error=None,
        content=winners
    )