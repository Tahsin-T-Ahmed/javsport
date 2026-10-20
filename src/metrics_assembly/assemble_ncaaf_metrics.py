import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def assemble_ncaaf_metrics(
    team_names_dict: dict,
    team_b_is_home: bool,
    leaderboards_dict: dict[str, pd.DataFrame],
    uploaded_files_dict: dict[str, pd.DataFrame]
) -> DataFrameMap:
    moneyline_df = uploaded_files_dict["moneyline"]
    cfbstats_glossary = pd.read_csv("./src/glossaries/ncaaf/teams_cfbstats.csv")
    metrics = pd.DataFrame()

    for team_key, team_name in team_names_dict.items():

        team_column_key = f"TEAM {team_key.upper()}"

        metrics.loc["team_name", team_column_key] = team_name

        for leaderboard_key, leaderboard in leaderboards_dict.items():
            match(leaderboard_key):
                case "dfei":
                    pass

                case "first_downs":
                    team_cfb_name = cfbstats_glossary.loc[
                        team_name == cfbstats_glossary["TEAMRANKINGS"].str.strip(),
                        "CFBSTATS"
                    ].item()

                    first_downs_per_game = leaderboard.loc[
                        team_cfb_name == leaderboard["TEAM CFB NAME"],
                        "PER GAME"
                    ].item()

                    metrics.loc["First Downs Per Game", team_column_key] = first_downs_per_game
                case _:
                    continue
                    return DataFrameMap(
                        error=f"Unrecognized leaderboard key: {leaderboard_key}",
                        content=None
                    )

    return DataFrameMap(
        error=None,
        content=metrics
    )
    