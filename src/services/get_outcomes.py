import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.builders.make_scoreboard import make_scoreboard
import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile

def get_outcomes(
    file: UploadedFile,
    progress_bar: DeltaGenerator | None = None
) -> DataFrameMap:
    errors = []

    wagers = pd.read_csv(file)
    n_wagers = wagers.shape[0]

    for wager_idx, wager_row in wagers.iterrows():
        if progress_bar:
            progress_bar.progress(
                text=f"Processing :violet[{wager_row['JAVSPORT PICK']}] vs :red[{wager_row['OPPONENT']}...]",
                value=wager_idx/n_wagers
            )

        scoreboard_map = make_scoreboard(wager_row["MATCH URL"])

        if scoreboard_map["error"]:
            errors.append(scoreboard_map["error"])
            continue

        scoreboard = scoreboard_map["content"]

        pick_score_match = scoreboard.loc[
            wager_row["JAVSPORT PICK"] == scoreboard["TEAM NAME"],
            "SCORE"
        ]

        opponent_score_match = scoreboard.loc[
            wager_row["OPPONENT"] == scoreboard["TEAM NAME"],
            "SCORE"
        ]

        if pick_score_match.empty or opponent_score_match.empty:
            continue

        wagers.loc[wager_idx, "PICK SCORE"] = pick_score_match.item()
        wagers.loc[wager_idx, "OPP SCORE"] = opponent_score_match.item()

    if progress_bar:
        progress_bar.status(
            label=":green[:material/check:] Outcomes Loaded!",
            state="complete"
        )

    return DataFrameMap(
        error=errors,
        content=wagers
    )