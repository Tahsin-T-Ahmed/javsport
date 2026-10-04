import streamlit as st

def generate_predictions(
    sport_key: str,
    metrics_assembler: callable
):
    schedule = st.session_state[sport_key]["schedule"]["data"]
    leaderboards = st.session_state[sport_key]["leaderboards"]
    uploaded_files = st.session_state[sport_key]["file_requirements"]["data"]

    for index, match_row in schedule.iterrows():
        team_names = dict(
            a=match_row["TEAM A"],
            b=match_row["TEAM B"]
        )

        metrics = metrics_assembler(
            team_names_dict=team_names,
            leaderboards_dict=leaderboards,
            uploaded_files_dict=uploaded_files
        )

        st.write(metrics)