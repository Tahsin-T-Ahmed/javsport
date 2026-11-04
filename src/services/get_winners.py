import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.services.get_match_winner import get_match_winner
from src.services.get_winner_picks import get_winner_picks
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile

def get_winners(
    file: UploadedFile,
    winner_picks_url: str | None,
    win_trends_df: pd.DataFrame | None,
    team_roster_df: pd.DataFrame | None,
    progress_bar: DeltaGenerator | None = None
) -> DataFrameMap:
    wagers = pd.read_csv(file)
    n_wagers = wagers.shape[0]

    # TESTING TEAM_ROSTER PARAM-ARG, REMOVE WHEN FINISHED
    if team_roster_df is not None:
        return DataFrameMap(
            error=None,
            content=team_roster_df
        )

    wagers["TRUE VICTOR"] = wagers["WINNER"].apply(
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

        # THIS IS TEMPORARY. REMOVE AFTER TESTING WIN-PICKS
        return DataFrameMap(
            error=None,
            content=winner_picks
        )

    wagers = wagers[["TRUE VICTOR", "WINNER", "OPPONENT", "CONFIDENCE", "MARKET ODDS", "EDGE", "MATCH URL"]]
    remaining_wagers = wagers[wagers["TRUE VICTOR"].isnull()]

    for wager_idx, wager_row in remaining_wagers.iterrows():
        if progress_bar:
            progress_bar.progress(
                value=wager_idx/n_wagers,
                text=f"Checking :violet[{wager_row['WINNER']}] vs :violet[{wager_row['OPPONENT']}]..."
            )
        true_victor = None

        victor_map = get_match_winner(wager_row["MATCH URL"])

        if victor_map["error"]:
            true_victor = victor_map["error"]
        else:
            true_victor = victor_map["content"]

        remaining_wagers.loc[wager_idx, "TRUE VICTOR"] = true_victor

    if progress_bar:
        progress_bar.status(
            label="Complete!",
            state="complete"
        )

    return DataFrameMap(
        error=None,
        content=remaining_wagers
    )