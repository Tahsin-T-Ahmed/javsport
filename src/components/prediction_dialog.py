import numpy as np
import pandas as pd
from src.components import table
from src.services.get_team_a_win_chance import get_team_a_win_chance
import streamlit as st

def render(
    sport_key: str,
    league_average: float,
    match_row: pd.Series,
    match_idx: int,
    leaderboards: dict[str, pd.DataFrame],
    uploaded_files: dict[str, pd.DataFrame],
    metrics_assembler: callable,
):
    with st.expander(
        label=f":orange[#{match_idx+1}:] :red[{match_row['TITLE']}]",
        expanded=True,
        type="default"
    ):
        team_names = dict(
            a=match_row["TEAM A"],
            b=match_row["TEAM B"]
        )

        team_b_is_home = match_row["TEAM B IS HOME"]

        metrics_map = metrics_assembler(
            team_names_dict=team_names,
            team_b_is_home=team_b_is_home,
            leaderboards_dict=leaderboards,
            uploaded_files_dict=uploaded_files
        )

        if metrics_map["error"]:
            st.info("This match is not worth calculating")
            st.error(
                body=metrics_map["error"],
                icon=":material/cancel:"
            )
            return

        metrics_df = metrics_map["content"]

        team_a_win_chance_map = get_team_a_win_chance(
            sport_key=sport_key,
            metrics_df=metrics_df,
            league_average=league_average
        )

        if team_a_win_chance_map["error"]:
            st.error(team_a_win_chance_map["error"])
            return

        team_a_win_chance = team_a_win_chance_map["content"]        
        team_b_win_chance = 1 - team_a_win_chance

        metrics_display_df = metrics_df.copy()        
        metrics_display_df.rename(
            index=lambda row: (
                " ".join([
                    term.capitalize()
                    if term not in ["ip", "siera"]
                    else term.upper()
                    for term in row.split("_")
                ])
            ),
            inplace=True
        )

        metrics_display_header = metrics_display_df.iloc[0, :]
        metrics_display_df.columns = metrics_display_header
        metrics_display_df = metrics_display_df.iloc[1:, :]
        
        table.render(
            data=metrics_display_df,
            label="Team Stats",
            collapse=True,
            height="content"
        )

        if team_a_win_chance > team_b_win_chance:
            st.write(f"{match_row['TEAM A']} :green[{np.round(team_a_win_chance*100, 2)}%]")
        elif team_b_win_chance > team_a_win_chance:
            st.write(f"{match_row['TEAM B']} :green[{np.round(team_b_win_chance*100, 2)}%]")
        else:
            st.write("COIN FLIP")