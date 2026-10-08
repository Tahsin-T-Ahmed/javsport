import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def assemble_mlb_metrics(
    team_names_dict: dict,
    team_b_is_home: bool,
    leaderboards_dict: dict[str, pd.DataFrame],
    uploaded_files_dict: dict[str, pd.DataFrame]
) -> DataFrameMap:
    metrics = pd.DataFrame()
    
    probable_pitchers_df = uploaded_files_dict["probable_pitchers"]
    siera_df = uploaded_files_dict["siera"]
    sp_df = uploaded_files_dict["starting_pitchers"]
    ip_df = uploaded_files_dict["innings_pitched"]

    for team_key, team_name in team_names_dict.items():
        pitchers_row = probable_pitchers_df[team_name == probable_pitchers_df["TR TEAM"]]

        if pitchers_row["N PITCHERS"].item() != 1:
            return DataFrameMap(
                error=f"Pitcher-count is not 1 for {team_name}",
                content=None
            )

        pitcher_name = pitchers_row["PITCHER 1"].item()
        pitcher_fgid = pitchers_row["PITCHER 1 FGID"].item()

        if not any(sp_df["FGID"].str.contains(pitcher_fgid)):
            return DataFrameMap(
                error=f"Pitcher is not Starting Pitcher (SP) for team {team_name}",
                content=None
            )

        pitcher_siera = siera_df.loc[pitcher_fgid == siera_df["PLAYER FGID"], "SIERA"].item()
        pitcher_ip = ip_df.loc[pitcher_fgid == ip_df["PLAYER FGID"], "IP"].item()

        team_column_key = f"TEAM {team_key.upper()}"

        metrics.loc["team_name", team_column_key] = team_name

        for leaderboard_key, leaderboard in leaderboards_dict.items():
            team_row = leaderboard[team_name == leaderboard["TEAM"]]

            if "win_trends" == leaderboard_key:
                team_total_games = team_row[["WINS", "LOSSES", "TIES"]].sum().sum()
                metrics.loc["total_games", team_column_key] = str(team_total_games)
                continue

            target_column = "AWAY"
            if "b" == team_key and team_b_is_home:
                target_column = "HOME"
                
            metrics.loc[leaderboard_key, team_column_key] = str(team_row[target_column].item())

        metrics.loc["pitcher_name", team_column_key] = pitcher_name

        metrics.loc["pitcher_siera", team_column_key] = str(pitcher_siera)

        metrics.loc["pitcher_ip", team_column_key] = str(pitcher_ip)

    return DataFrameMap(
        error=None,
        content=metrics
    )