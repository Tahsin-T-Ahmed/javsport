import pandas as pd
import requests
import streamlit as st

from src.data_collection.scrapers.scan_bcftoys_table import scan_bcftoys_table

mytable = scan_bcftoys_table("https://bcftoys.com/2026-ofei")["content"]
st.write(mytable)

session_state_view = st.empty()

metrics_df = pd.DataFrame()

columns = st.columns(2)

for col_idx, column in enumerate(columns):
    team_letter = None
    if 0 == col_idx:
        team_letter = "a"
    if 1 == col_idx:
        team_letter = "b"

    key_counter = 0

    with column:
        st.subheader(f"Team {team_letter.upper()}")

        dfei = st.number_input(
            label="DFEI",
            key=f"{key_counter}{team_letter}"
        )
        key_counter+=1
        field_goal_attempts_per_game = st.number_input(
            label="Field Goal Attempts Per Game",
            key=f"{key_counter}{team_letter}"
        )
        key_counter+=1
        first_downs_per_game = st.number_input(
            label="First Downs Per Game",
            key=f"{key_counter}{team_letter}"
        )
        key_counter+=1
        giveaways_per_game = st.number_input(
            label="Giveaways Per Game",
            key=f"{key_counter}{team_letter}"
        )
        key_counter+=1
        punt_attempts_per_game = st.number_input(
            label="Punt Attempts Per Game",
            key=f"{key_counter}{team_letter}"
        )
        key_counter+=1
        yards_per_game = st.number_input(
            label="Yards Per Game",
            key=f"{key_counter}{team_letter}"
        )

        metrics_df.loc["dfei", f"TEAM {team_letter.upper()}"] = dfei
        metrics_df.loc["field_goal_attempts_per_game", f"TEAM {team_letter.upper()}"] = field_goal_attempts_per_game
        metrics_df.loc["first_downs_per_game", f"TEAM {team_letter.upper()}"] = first_downs_per_game
        metrics_df.loc["giveaways_per_game", f"TEAM {team_letter.upper()}"] = giveaways_per_game
        metrics_df.loc["punt_attempts_per_game", f"TEAM {team_letter.upper()}"] = punt_attempts_per_game
        metrics_df.loc["yards_per_game", f"TEAM {team_letter.upper()}"] = yards_per_game

if st.button("Go"):
    st.write(metrics_df)
    javsport_url = f"http://127.0.0.1:5000/ncaaf/predict-team-a-win-chance"

    response = requests.get(
        url=javsport_url,
        params=dict(
            metrics_json=metrics_df.to_json()
        )
    )

    if 200 == response.status_code:
        st.write(response.text)
    else:
        st.error("Invalid response received")
        st.html(response.text)

# session_state_view.write(st.session_state)