import pandas as pd
from src.data_collection.data_maps import StringMap
import streamlit as st

team_name_glossary = pd.read_csv("./assets/mlb_team_name_glossary.csv")

leaderboards = st.session_state["mlb"]["leaderboards"]

probable_pitchers_df = st.session_state["mlb"]["file_requirements"]["data"]["probable_pitchers"]
starting_pitchers_df = st.session_state["mlb"]["file_requirements"]["data"]["starting_pitchers"]
siera_df = st.session_state["mlb"]["file_requirements"]["data"]["siera"]
innings_pitched_df = st.session_state["mlb"]["file_requirements"]["data"]["innings_pitched"]

def predict_mlb_match(
    match_row: pd.Series,
    league_avg_runs: float,
) -> StringMap:
    st.write(starting_pitchers_df)
    team_b_is_home = match_row["TEAM B IS HOME"]

    team_names = dict(
        a=match_row["TEAM A"],
        b=match_row["TEAM B"]
    )

    metrics = dict()

    for team_key, team_name in team_names.items():

        metrics[f"team_name_{team_key}"] = team_name

        team_fg_name = team_name_glossary.loc[
            team_name == team_name_glossary["TEAMRANKINGS"].str.strip(),
            "FANGRAPHS"
        ].item()

        pitchers_row = probable_pitchers_df[team_fg_name == probable_pitchers_df["TEAM"]]

        if pitchers_row["N PITCHERS"].item() != 1:
            return StringMap(
                error=f"Invalid pitcher-count in match {match_row['TITLE']}",
                content=None
            )

        pitcher_name = pitchers_row["PITCHER 1"].item()

        st.write(pitcher_name)
        continue

        if not starting_pitchers_df["NAME"].str.contains(pitcher_name):
            return StringMap(
                error=f"Pitcher is not Starting Pitcher (SP) in match {match_row['TITLE']}",
                content=None
            )

        for leaderboard_key, leaderboard in leaderboards.items():
            target_column = "AWAY"
            if team_b_is_home and "b" == team_key:
                target_column = "HOME"

            team_row = leaderboard[team_name == leaderboard["TEAM"]]

            if "runs_per_game" == leaderboard_key:
                continue

            if "win_trends" == leaderboard_key:
                team_total_games = team_row[["WINS", "LOSSES", "TIES"]].sum().sum()
                metrics[f"total_games_{team_key}"] = team_total_games
            else:            
                metrics[f"{leaderboard_key}_{team_key}"] = team_row[target_column].item()

    metrics["league_avg_runs"] = league_avg_runs

    st.divider()

    return metrics