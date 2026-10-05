import json
import numpy as np
import requests
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

    api_url = f"http://127.0.0.1:5000/{sport_key}/predict-team-a-win-chance"

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

        metrics_json = metrics_df.to_json()

        params = dict(
            league_average=league_average,
            metrics_json=metrics_json
        )

        # st.write(params)

        response = requests.get(
            url=api_url,
            params=params
        )

        if 200 != response.status_code:
            st.error(f"ERROR: Invalid status code {response.status_code} from URL {api_url}")
            # st.html(response.text)
            continue

        team_a_win_chance = float(response.text)
        team_b_win_chance = 1 - team_a_win_chance

        display_time = (
            st.session_state[sport_key]
            ["schedule"]
            ["display"]
            .loc[match_index, "TIME"]
        )

        with st.container(border=True):

            st.markdown(
                body=(
                    f"#### :orange[#{match_index}:] :red[{match_row['TITLE']}] ({display_time})"
                ),
                anchors=False
            )

            if team_a_win_chance > team_b_win_chance:
                st.write(
                    f"Winner: {match_row['TEAM A']} (:green[{np.round(team_a_win_chance * 100, 2)}%] confidence)"
                )
            elif team_b_win_chance > team_a_win_chance:
                st.write(
                    f"Winner: {match_row['TEAM B']} (:green[{np.round(team_b_win_chance * 100, 2)}%] confidence)"
                )
            else:
                st.write("No clear winner (coin-flip)")

            st.markdown("#### Market says:")
            st.write(
                uploaded_files["moneyline"].loc[
                    match_row["TEAM A"] == uploaded_files["moneyline"]["TEAM"]
                ]
            )