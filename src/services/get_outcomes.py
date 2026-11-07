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
    progress_bar: DeltaGenerator | None = None
) -> DataFrameMap:
    wagers = pd.read_csv(file)
    n_wagers = wagers.shape[0]

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
            if progress_bar:
                progress_bar.progress(
                    text=f"Processing :violet[{wager_row['WINNER']}] vs :red[{wager_row['OPPONENT']}...]",
                    value=wager_idx/n_wagers
                )

            winpick_row = winner_picks[
                winner_picks["MATCH URL"] == wager_row["MATCH URL"]
            ]

            if winpick_row.empty:
                continue

            winpick_status = winpick_row["STATUS"].item().strip().upper()
            winpick_favorite = winpick_row["FAVORITE"].item().strip().upper()
            javsport_winner = wager_row["WINNER"].item().strip().upper()

            if javsport_winner == winpick_favorite:
                wagers.loc[wager_idx, "STATUS"] = winpick_status.item().upper()
                continue

            if "RIGHT" == winpick_status:
                wagers.loc[wager_idx, "STATUS"] = "WRONG"

    wagers_to_scrape = wagers[wagers["STATUS"].isnull()]

    for wager_idx, wager_row in wagers_to_scrape.iterrows():
        if progress_bar:
            progress_bar.progress(
                text=f"Processing :violet[{wager_row['WINNER']}] vs :red[{wager_row['OPPONENT']}...]",
                value=wager_idx/n_wagers
            )
            
        winning_team_map = get_match_winner(wager_row["MATCH URL"])

        if winning_team_map["error"]:
            st.error(winning_team_map["error"])
            continue

        winning_team = winning_team_map["content"].strip()

        if wager_row["WINNER"] == winning_team:
            wagers.loc[wager_idx, "STATUS"] = "RIGHT"
        else:
            wagers.loc[wager_idx, "STATUS"] = "WRONG"

    if progress_bar:
        progress_bar.status(
            label=":green[:material/check:] Outcomes Loaded!",
            state="complete"
        )

    return DataFrameMap(
        error=None,
        content=wagers
    )