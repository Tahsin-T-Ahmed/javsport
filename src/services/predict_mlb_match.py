import pandas as pd
import requests
from src.data_collection.data_maps import StringMap
import streamlit as st

team_name_glossary = pd.read_csv("./assets/mlb_team_name_glossary.csv")

def predict_mlb_match(
    match_row: pd.Series,
    league_avg_runs: float,
    probable_pitchers_df: pd.DataFrame,
    sp_df: pd.DataFrame,
    siera_df: pd.DataFrame,
    innings_pitched_df: pd.DataFrame,
    leaderboards: pd.DataFrame
) -> StringMap:
    team_b_is_home = match_row["TEAM B IS HOME"]
    st.header(match_row["TITLE"])

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
                error=f"Pitcher-count is not 1 in game: {match_row['TITLE']}",
                content=None
            )

        pitcher_fgid = pitchers_row["PITCHER 1 FGID"].item()

        if not any(sp_df["FGID"].str.contains(pitcher_fgid)):
            return StringMap(
                error=f"Pitcher is not Starting Pitcher (SP) in match {match_row['TITLE']}",
                content=None
            )

        pitcher_siera = siera_df.loc[pitcher_fgid == siera_df["PLAYER FGID"], "SIERA"].item()

        metrics[f"pitcher_siera_{team_key}"] = pitcher_siera

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

    

    response = requests.get(
        url="http://127.0.0.1:5000/mlb/predict-team-a-win-chance",
        params=metrics
    )

    # st.divider()

    if 200 == response.status_code:

        return response.text