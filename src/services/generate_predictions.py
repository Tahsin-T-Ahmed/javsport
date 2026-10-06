import json
import numpy as np
from src.services.get_team_a_win_chance import get_team_a_win_chance
import streamlit as st

def generate_predictions(
    sport_key: str,
    metrics_assembler: callable
):
    schedule = st.session_state[sport_key]["schedule"]["data"]
    leaderboards = st.session_state[sport_key]["leaderboards"]
    uploaded_files = st.session_state[sport_key]["file_requirements"]["data"]
    
    league_points_df_name = None

    match(sport_key.upper()):
        case "MLB":
            league_points_df_name = "runs_per_game"

        case "NBA" | "NCAAB" | "WNBA":
            league_points_df_name = "points_per_game"

        case "NFL" | "NCAAF":
            league_points_df_name = "touchdowns_per_game"
            
        case _:
            st.error(f"Invalid SPORT KEY {sport_key}")
            return

    league_average = (
        st.session_state
        [sport_key]
        ["leaderboards"]
        [league_points_df_name]
        ["OVERALL"]
        .mean()
    )

    for match_index, match_row in schedule.iterrows():
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
            st.error(metrics_map["error"])
            continue

        metrics_df = metrics_map["content"]

        team_a_win_chance_map = get_team_a_win_chance(
            sport_key=sport_key,
            metrics_df=metrics_df,
            league_average=league_average
        )

        if team_a_win_chance_map["error"]:
            st.error(team_a_win_chance_map["error"])
            continue

        team_a_win_chance = team_a_win_chance_map["content"]
        
        team_b_win_chance = 1 - team_a_win_chance

        st.write("TEAM A:")
        st.write(f"{match_row['TEAM A']}: :green[{team_a_win_chance}]")

        st.write("TEAM B:")
        st.write(f"{match_row['TEAM B']}: :orange[{team_b_win_chance}]")