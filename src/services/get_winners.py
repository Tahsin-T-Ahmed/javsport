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

    wagers["TRUE VICTOR"] = wagers["WINNER"].apply(
        lambda x: None
    )

    if winner_picks_url:
        if win_trends_df is None:
            return DataFrameMap(
                error=f"ERROR (Winners-Getter): Missing Win-Trends DataFrame",
                content=None
            )

        if team_roster_df is None:
            return DataFrameMap(
                error=f"ERROR (Winners-Getter): Missing Team-Roster DataFrame",
                content=None
            )
        
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
            winpick_status = winner_picks.loc[
                winner_picks["MATCH URL"] == wager_row["MATCH URL"],
                "STATUS"
            ].item().strip().upper()

    # wagers = wagers[["TRUE VICTOR", "WINNER", "OPPONENT", "CONFIDENCE", "MARKET ODDS", "EDGE", "MATCH URL"]]
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

        wagers.loc[wager_idx, "TRUE VICTOR"] = true_victor

    if progress_bar:
        progress_bar.status(
            label="Complete!",
            state="complete"
        )

    return DataFrameMap(
        error=None,
        content=wagers
    )