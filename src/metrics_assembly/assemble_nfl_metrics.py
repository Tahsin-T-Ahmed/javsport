import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def assemble_nfl_metrics(
    team_names_dict: dict,
    team_b_is_home: bool,
    leaderboards_dict: dict[str, pd.DataFrame],
    uploaded_files_dict: dict[str, pd.DataFrame]
) -> DataFrameMap:
    dave_df = uploaded_files_dict["dave"]
    ftn_glossary = pd.read_csv("./src/glossaries/nfl/teams_ftnfantasy.csv")

    metrics = pd.DataFrame()

    for team_key, team_name in team_names_dict.items():

        team_column_key = f"TEAM {team_key.upper()}"

        metrics.loc["team_name", team_column_key] = team_name

        for leaderboard_key, leaderboard in leaderboards_dict.items():
            team_row = leaderboard[team_name == leaderboard["TEAM NAME"]]

            if "win_trends" == leaderboard_key:
                team_total_games = team_row[["WINS", "LOSSES", "TIES"]].sum().sum()
                metrics.loc["total_games", team_column_key] = str(team_total_games)
                continue

            target_column = "AWAY"
            if "b" == team_key and team_b_is_home:
                target_column = "HOME"
                
            metrics.loc[leaderboard_key, team_column_key] = str(team_row[target_column].item())

        team_ftn_name = ftn_glossary.loc[
            team_name == ftn_glossary["TEAMRANKINGS"].str.strip(),
            "FTNFANTASY"
        ].item()

        team_dave_off = dave_df.loc[
            team_ftn_name == dave_df["TEAM"],
            "OFF DAVE"
        ].item()

        team_dave_def = dave_df.loc[
            team_ftn_name == dave_df["TEAM"],
            "DEF DAVE"
        ].item()

        metrics.loc["dave_offense", team_column_key] = str(team_dave_off)
        metrics.loc["dave_defense", team_column_key] = str(team_dave_def)

    return DataFrameMap(
        error=None,
        content=metrics
    )
    