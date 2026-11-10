import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.services.get_match_winner import get_match_winner
from src.services.get_winner_picks import get_winner_picks
import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile

def get_outcomes(
    file: UploadedFile,
    winner_picks_url: str | None,
    team_roster_df: pd.DataFrame,
    win_trends_df: pd.DataFrame,
    progress_bar: DeltaGenerator | None = None
) -> DataFrameMap:
    wagers = pd.read_csv(file)
    n_wagers = wagers.shape[0]

    wagers["STATUS"] = wagers["JAVSPORT PICK"].apply(
        lambda x: None
    )

    completed_wagers = 0

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
            if progress_bar:
                progress_bar.progress(
                    text=f"Processing :violet[{wager_row['JAVSPORT PICK']}] vs :red[{wager_row['OPPONENT']}...]",
                    value=completed_wagers/n_wagers
                )

            winpick_row = winner_picks[
                winner_picks["MATCH URL"] == wager_row["MATCH URL"]
            ]

            if winpick_row.empty:
                continue

            winpick_status = winpick_row["STATUS"].item().strip().upper()
            market_pick = winpick_row["MARKET PICK"].item().strip().upper()

            javsport_winner_fullname = wager_row["JAVSPORT PICK"].strip().upper()
            
            javsport_winner_trid = team_roster_df.loc[
                wager_row["JAVSPORT PICK"] == team_roster_df["TEAM NAME"],
                "TEAM TRID"
            ].item()

            javsport_winner_shortname = win_trends_df.loc[
                javsport_winner_trid == win_trends_df["TEAM TRID"],
                "TEAM NAME"
            ].item().strip().upper()

            outcome = None

            if javsport_winner_shortname == market_pick:
                outcome = winpick_status
            else:
                if "RIGHT" == winpick_status:
                    outcome = "WRONG"

            wagers.loc[wager_idx, "STATUS"] = outcome

            if outcome:
                completed_wagers += 1

    wagers_to_scrape = wagers[wagers["STATUS"].isnull()]

    for wager_idx, wager_row in wagers_to_scrape.iterrows():
        if progress_bar:
            progress_bar.progress(
                text=f"Processing :violet[{wager_row['JAVSPORT PICK']}] vs :red[{wager_row['OPPONENT']}...]",
                value=completed_wagers/n_wagers
            )
            
        winning_team_map = get_match_winner(wager_row["MATCH URL"])

        if winning_team_map["error"]:
            st.error(winning_team_map["error"])
            continue

        winning_team = winning_team_map["content"].strip()

        outcome = None

        if wager_row["JAVSPORT PICK"] == winning_team:
            outcome = "RIGHT"
        else:
            outcome = "WRONG"

        wagers.loc[wager_idx, "STATUS"] = outcome
        completed_wagers += 1

    if progress_bar:
        progress_bar.status(
            label=":green[:material/check:] Outcomes Loaded!",
            state="complete"
        )

    return DataFrameMap(
        error=None,
        content=wagers
    )