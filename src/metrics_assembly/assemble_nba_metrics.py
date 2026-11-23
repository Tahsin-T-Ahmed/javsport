import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def assemble_nba_metrics(
    team_names_dict: dict,
    team_b_is_home: bool,
    leaderboards_dict: dict[str, pd.DataFrame],
    uploaded_files_dict: dict[str, pd.DataFrame]
) -> DataFrameMap:
    metrics = pd.DataFrame()

    xpm_df = uploaded_files_dict["team_xpm"]

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

        xpm_row = xpm_df[team_name == xpm_df["TEAM TR NAME"]]

        xpm_offense = xpm_row["XPM OFFENSE"].item()
        xpm_defense = xpm_row["XPM DEFENSE"].item()

        metrics.loc["xpm_offense", team_column_key] = str(xpm_offense)
        metrics.loc["xpm_defense", team_column_key] = str(xpm_defense)

    return DataFrameMap(
        error=None,
        content=metrics
    )