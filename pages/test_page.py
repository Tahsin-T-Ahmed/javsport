import requests
from src.data_collection.parsers.scan_mlb_starting_pitchers import scan_mlb_starting_pitchers
import streamlit as st

session_state_view = st.empty()

league_avg_runs = st.number_input("League Avg Runs")

javsport_params = dict(
    league_avg_runs=league_avg_runs
)

columns = st.columns(2)

for col_idx, column in enumerate(columns):
    team_letter = None
    if 0 == col_idx:
        team_letter = "_a"
    if 1 == col_idx:
        team_letter = "_b"

    with column:
        at_bats_per_game = st.number_input(
            label="At Bats",
            key=f"at_bats_per_game{team_letter}"
        )
        hits_per_game = st.number_input(
            label="Hits",
            key=f"hits_per_game{team_letter}"
        )
        home_runs_per_game = st.number_input(
            label="Home Runs",
            key=f"home_runs_per_game{team_letter}"
        )
        total_bases_per_game = st.number_input(
            label="Total Bases",
            key=f"total_bases_per_game{team_letter}"
        )
        walks_per_game = st.number_input(
            label="Walks",
            key=f"walks_per_game{team_letter}"
        )
        total_games = st.number_input(
            label="Total Games",
            key=f"total_games{team_letter}"
        )
        pitcher_siera = st.number_input(
            label="SIERA",
            key=f"pitcher_siera{team_letter}"
        )

        javsport_params[f"at_bats_per_game{team_letter}"] = at_bats_per_game
        javsport_params[f"hits_per_game{team_letter}"] = hits_per_game
        javsport_params[f"home_runs_per_game{team_letter}"] = home_runs_per_game
        javsport_params[f"total_bases_per_game{team_letter}"] = total_bases_per_game
        javsport_params[f"walks_per_game{team_letter}"] = walks_per_game
        javsport_params[f"total_games{team_letter}"] = total_games
        javsport_params[f"pitcher_siera{team_letter}"] = pitcher_siera

if st.button("Go"):
    # st.write(javsport_params)
    javsport_url = f"http://127.0.0.1:5000/mlb/predict-team-a-win-chance"

    response = requests.get(
        url=javsport_url,
        params=javsport_params
    )

    if 200 == response.status_code:
        st.write(response.text)
    else:
        st.error("Invalid response received")
        st.html(response.text)

session_state_view.write(st.session_state)