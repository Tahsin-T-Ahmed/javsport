import json
import requests
import streamlit as st

session_state_view = st.empty()

# league_avg_runs = st.number_input("League Avg Runs")

javsport_params = dict(
    # league_avg_runs=league_avg_runs
    metrics_json = {
        "TEAM A": dict(),
        "TEAM B": dict()
    }
)

columns = st.columns(2)

for col_idx, column in enumerate(columns):
    team_letter = None
    if 0 == col_idx:
        team_letter = "a"
    if 1 == col_idx:
        team_letter = "b"

    with column:

        st.header(f"TEAM {team_letter.upper()}")

        counter = 0
        
        first_downs = st.number_input(
            label="First Downs Per Game",
            key=f"{counter}{team_letter}"
        )

        counter += 1

        total_yards = st.number_input(
            label="Total Yards",
            key=f"{counter}{team_letter}"
        )

        counter += 1

        giveaways = st.number_input(
            label="Giveaways Per Game",
            key=f"{counter}{team_letter}"
        )

        counter += 1

        punts = st.number_input(
            label="Punt Attempts Per Game",
            key=f"{counter}{team_letter}"
        )

        counter += 1

        fga = st.number_input(
            label="Field Goal Attempts Per Game",
            key=f"{counter}{team_letter}"
        )

        counter += 1

        special_off = st.number_input(
            label="FEI Offense",
            key=f"{counter}{team_letter}"
        )

        counter += 1

        special_def = st.number_input(
            label="FEI Defense",
            key=f"{counter}{team_letter}"
        )

        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"first_downs_per_game"] = first_downs
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"yards_per_game"] = total_yards
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"giveaways_per_game"] = giveaways
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"punt_attempts_per_game"] = punts
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"field_goal_attempts_per_game"] = fga
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"special_offense"] = special_off
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"special_defense"] = special_def

if st.button("Go"):
    javsport_params["metrics_json"] = json.dumps(javsport_params["metrics_json"])
    st.write(javsport_params)
    javsport_url = f"http://127.0.0.1:5000/ncaaf/predict-team-a-win-chance"

    response = requests.get(
        url=javsport_url,
        params=javsport_params
    )

    if 200 == response.status_code:
        st.write(response.text)
    else:
        st.error("Invalid response received")
        st.html(response.text)