import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def assemble_ncaaf_metrics(
    team_names_dict: dict,
    team_b_is_home: bool,
    leaderboards_dict: dict[str, pd.DataFrame],
    uploaded_files_dict: dict[str, pd.DataFrame]
) -> DataFrameMap:
    moneyline_df = uploaded_files_dict["moneyline"]
    bcftoys_glossary = pd.read_csv("./src/glossaries/ncaaf/teams_bcftoys.csv")
    cfbstats_glossary = pd.read_csv("./src/glossaries/ncaaf/teams_cfbstats.csv")
    
    metrics = pd.DataFrame()

    for team_key, team_name in team_names_dict.items():

        team_column_key = f"TEAM {team_key.upper()}"

        metrics.loc["team_name", team_column_key] = team_name

        for leaderboard_key, leaderboard in leaderboards_dict.items():
            metric = None
            match(leaderboard_key):
                case "dfei":
                    team_bcf_name = bcftoys_glossary.loc[
                        team_name == bcftoys_glossary["TEAMRANKINGS"].str.strip(),
                        "BCFTOYS"
                    ].item()

                    team_dfei = leaderboard.loc[
                        team_bcf_name == leaderboard["TEAM BCF NAME"],
                        "DFEI"
                    ].item()

                    metric = str(team_dfei)

                case "first_downs_per_game":
                    team_cfb_name = cfbstats_glossary.loc[
                        team_name == cfbstats_glossary["TEAMRANKINGS"].str.strip(),
                        "CFBSTATS"
                    ].item()

                    first_downs_per_game = leaderboard.loc[
                        team_cfb_name == leaderboard["TEAM CFB NAME"],
                        "PER GAME"
                    ].item()

                    metric = str(first_downs_per_game)

                case (
                    "field_goal_attempts_per_game" |
                    "giveaways_per_game" |
                    "punt_attempts_per_game" |
                    "yards_per_game"
                ):
                    target_column = "AWAY"
                    if "b" == team_key and team_b_is_home:
                        target_column = "HOME"

                    metric = leaderboard.loc[
                        team_name == leaderboard["TEAM NAME"],
                        target_column
                    ].item()

                    metric = str(metric)

                case "win_trends":
                    continue
                
                case _:
                    return DataFrameMap(
                        error=f"Unrecognized leaderboard key: {leaderboard_key}",
                        content=None
                    )

            metrics.loc[leaderboard_key, team_column_key] = metric

    return DataFrameMap(
        error=None,
        content=metrics
    )
    