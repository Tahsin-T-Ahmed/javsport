import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.services.get_winner_picks import get_winner_picks
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile

def get_outcomes(
    file: UploadedFile,
    winner_picks_url: str | None,
    progress_bar: DeltaGenerator | None = None
) -> DataFrameMap:
    wagers = pd.read_csv(file)

    wagers["STATUS"] = wagers["WINNER"].apply(
        lambda x: None
    )

    if winner_picks_url:
        winner_picks_map = get_winner_picks(winner_picks_url)

        if winner_picks_map["error"]:
            return DataFrameMap(
                error=winner_picks_map["error"],
                content=None
            )

        winner_picks = winner_picks_map["content"]

        winner_picks["MATCH URL"] = winner_picks["MATCH URL"].apply(
            lambda url_path: f"https://www.teamrankings.com{url_path}"
        )

        for wager_idx, wager_row in wagers.iterrows():
            winpick_row = winner_picks[
                winner_picks["MATCH URL"] == wager_row["MATCH URL"]
            ]

            if winpick_row.empty:
                continue

            winpick_status = winpick_row["STATUS"]
            wagers.loc[wager_idx, "STATUS"] = winpick_status.item().upper()

    return DataFrameMap(
        error=None,
        content=wagers
    )