import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.services.get_match_winner import get_match_winner
import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile

def get_outcomes(
    file: UploadedFile,
    progress_bar: DeltaGenerator | None = None
) -> DataFrameMap:
    wagers = pd.read_csv(file)
    n_wagers = wagers.shape[0]

    wagers["STATUS"] = wagers["JAVSPORT PICK"].apply(
        lambda x: None
    )

    for wager_idx, wager_row in wagers.iterrows():
        if progress_bar:
            progress_bar.progress(
                text=f"Processing :violet[{wager_row['JAVSPORT PICK']}] vs :red[{wager_row['OPPONENT']}...]",
                value=wager_idx/n_wagers
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

    if progress_bar:
        progress_bar.status(
            label=":green[:material/check:] Outcomes Loaded!",
            state="complete"
        )

    return DataFrameMap(
        error=None,
        content=wagers
    )