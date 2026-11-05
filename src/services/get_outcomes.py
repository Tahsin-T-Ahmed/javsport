import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.services.get_winners import get_winners
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile

def get_outcomes(
    file: UploadedFile,
    winner_picks_url: str | None,
    win_trends_df: pd.DataFrame | None,
    team_roster_df: pd.DataFrame | None,
    progress_bar: DeltaGenerator | None = None
) -> DataFrameMap:
    winners_map = get_winners(
        file=file,
        winner_picks_url=winner_picks_url,
        win_trends_df=win_trends_df,
        team_roster_df=team_roster_df,
        progress_bar=progress_bar
    )

    if winners_map["error"]:
        return DataFrameMap(
            error=winners_map["error"],
            content=None
        )

    winners = winners_map["content"]

    outcomes = winners

    outcomes.rename(
        columns={
            "WINNER": "CHOSEN TEAM"
        },
        inplace=True
    )

    outcomes["OUTCOME"] = outcomes.apply(
        lambda row: "RIGHT" if row["CHOSEN TEAM"] == row["TRUE VICTOR"] else "WRONG",
        axis=1
    )

    outcomes = outcomes[["OUTCOME", "CHOSEN TEAM", "OPPONENT", "CONFIDENCE", "MARKET ODDS", "EDGE"]]

    return DataFrameMap(
        error=None,
        content=outcomes
    )