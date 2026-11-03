from src.data_collection.builders.make_winner_picks import make_winner_picks
from src.data_collection.data_maps import DataFrameMap
from streamlit.typing import UploadedFile

def get_winner_picks(
    file: UploadedFile,
    winner_picks_url: str | None,
    month: int | str,
    day: int | str,
) -> DataFrameMap:
    if winner_picks_url:
        winner_picks_map = make_winner_picks(
            url=winner_picks_url,
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

    winner_picks = None

    return DataFrameMap(
        error=None,
        content=winner_picks
    )