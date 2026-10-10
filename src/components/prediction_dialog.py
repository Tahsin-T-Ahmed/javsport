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
    team_roster: pd.DataFrame,
    uploaded_files: dict[str, pd.DataFrame],
    metrics_assembler: callable,
):
    team_names = dict(
        a=match_row["TEAM A"],
        b=match_row["TEAM B"]
    )

    team_b_is_home = match_row["TEAM B IS HOME"]

    display_time = (
        st.session_state[sport_key]["schedule"]["display"].loc[
            match_idx, "TIME"
        ]
    )

    team_full_names = dict()

    for team_key, team_name in team_names.items():
        team_trid = leaderboards["win_trends"][
            team_name == leaderboards["win_trends"]["TEAM NAME"]
        ].index.item()

        team_full_name = team_roster.loc[
            team_trid, "TEAM NAME"
        ]

        team_full_names[team_key] = team_full_name
        
    with st.expander(
        label=f":red[{match_idx+1}/{st.session_state[sport_key]["schedule"]["data"].shape[0]}:] :orange[{display_time}] :violet[{team_full_names['a']} vs {team_full_names['b']}]",
        expanded=True,
        type="default"
    ):
        metrics_map = metrics_assembler(
            team_names_dict=team_names,
            team_b_is_home=team_b_is_home,
            leaderboards_dict=leaderboards,
            uploaded_files_dict=uploaded_files
        )

        if metrics_map["error"]:
            st.info(
                body=f"This match is not worth calculating",
                icon=":material/thumb_down:"
            )
            st.warning(
                body = f"Why? :red[{metrics_map['error']}]",
                icon=":material/sentiment_dissatisfied:"
            )
            return

        metrics_df = metrics_map["content"]

        team_win_chances = dict()

        with st.spinner("Loading Win-Probability..."):
            team_a_win_chance_map = get_team_a_win_chance(
                sport_key=sport_key,
                metrics_df=metrics_df,
                league_average=league_average
            )

            if team_a_win_chance_map["error"]:
                st.error(team_a_win_chance_map["error"])
                return
            team_win_chances["a"] = team_a_win_chance_map["content"] 
            team_win_chances["b"] = 1 - team_win_chances["a"]

        winning_team_key = None

        if team_win_chances["a"] > team_win_chances["b"]:
            winning_team_key = "a"
        elif team_win_chances["b"] > team_win_chances["a"]:
            winning_team_key = "b"
        else:
            winning_team_key = None

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

        team_moneylines = dict()
        for team_key, team_name in team_names.items():
            team_moneylines[team_key] = (
                uploaded_files["moneyline"].loc[
                    team_name == uploaded_files["moneyline"]["TEAM"],
                    "PROBABILITY"
                ]
            ).item()

        st.markdown(
            body=f"##### :orange[:material/trophy:] JavSport thinks :violet[{team_names[winning_team_key]}] will win :orange[:material/trophy:]",
            anchors=False
        )

        st.write(f"JavSport's confidence: :violet[{np.round(team_win_chances[winning_team_key]*100, 2)}%]")
        st.write(f"While the Market says: :orange[{np.round(team_moneylines[winning_team_key]*100, 2)}%]")

        edge = np.round(
            (team_win_chances[winning_team_key] - team_moneylines[winning_team_key])*100,
            2
        )

        if np.abs(edge) >= 0.5:
            edge_color = None

            if team_win_chances[winning_team_key] < team_moneylines[winning_team_key]:
                edge_color = "red"
            else:
                edge_color = "green"

            st.write(f"Edge against the Market: :{edge_color}[{'+' if edge > 0 else ''}{edge}%]")
        else:
            st.caption("Predictions are similar")
        
        table.render(
            data=metrics_display_df,
            label="Team Stats",
            collapse=True,
            height="content",
            expanded=False
        )