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
        
        fga = st.number_input(
            label="Field Goals Attempted",
            key=f"field_goals_attempted_per_game{team_letter}"
        )
        fgm = st.number_input(
            label="Field Goals Made",
            key=f"field_goals_made_per_game{team_letter}"
        )
        ftm = st.number_input(
            label="Free Throws Made",
            key=f"free_throws_made_per_game{team_letter}"
        )
        tov = st.number_input(
            label="Turnovers",
            key=f"turnovers_per_game{team_letter}"
        )
        orb = st.number_input(
            label="Offensive Rebounds",
            key=f"offensive_rebounds_per_game{team_letter}"
        )
        drb = st.number_input(
            label="Defense Rebounds",
            key=f"defensive_rebounds_per_game{team_letter}"
        )
        xpm_offense = st.number_input(
            label="XPM Offense",
            key=f"xpm_offense{team_letter}"
        )
        xpm_defense = st.number_input(
            label="XPM Defense",
            key=f"xpm_defense{team_letter}"
        )

        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"field_goals_attempted_per_game"] = fga
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"field_goals_made_per_game"] = fgm
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"free_throws_made_per_game"] = ftm
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"turnovers_per_game"] = tov
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"offensive_rebounds_per_game"] = orb
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"defensive_rebounds_per_game"] = drb
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"xpm_offense"] = xpm_offense
        javsport_params["metrics_json"][f"TEAM {team_letter.upper()}"][f"xpm_defense"] = xpm_defense

if st.button("Go"):
    javsport_params["metrics_json"] = json.dumps(javsport_params["metrics_json"])
    st.write(javsport_params)
    javsport_url = f"http://127.0.0.1:5000/nba/predict-team-a-win-chance"

    response = requests.get(
        url=javsport_url,
        params=javsport_params
    )

    if 200 == response.status_code:
        st.write(response.text)
    else:
        st.error("Invalid response received")
        st.html(response.text)