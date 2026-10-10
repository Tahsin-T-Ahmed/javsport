from src.components import prediction_dialog
import streamlit as st

def generate_predictions(
    sport_key: str,
    metrics_assembler: callable
):
    schedule = st.session_state[sport_key]["schedule"]["data"]
    leaderboards = st.session_state[sport_key]["leaderboards"]
    team_roster = st.session_state[sport_key]["team_roster"]
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

    for match_idx, match_row in schedule.iterrows():
        prediction_dialog.render(
            sport_key=sport_key,
            league_average=league_average,
            match_row=match_row,
            match_idx=match_idx,
            leaderboards=leaderboards,
            team_roster=team_roster,
            uploaded_files=uploaded_files,
            metrics_assembler=metrics_assembler
        )