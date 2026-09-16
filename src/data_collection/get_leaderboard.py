from datetime import datetime
import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scan_table import scan_table

def get_leaderboard(leaderboard_url:str, timestamp: datetime.datetime) -> DataFrameMap:
    year, month, day = f"{timestamp.year:04d}", f"{timestamp.month:02d}", f"{timestamp.day:02d}"
    date_str = f"{year}-{month}-{day}"

    leaderboard_map = scan_table(f"{leaderboard_url}?date={date_str}")
    if leaderboard_map["error"]:
        return dict(
            error = leaderboard_map["error"],
            content = None
        )

    leaderboard = leaderboard_map["content"]

    leaderboard["TEAM ID"] = leaderboard["TEAM_LINK"].apply(
        lambda link: link.split("/")[-1]
    )

    leaderboard.drop(
        columns = [
            *leaderboard.columns[:9],
            leaderboard.columns[10]
        ],
        inplace = True
    )

    leaderboard.columns = [column.replace("_DATASORT", "") for column in leaderboard.columns]

    leaderboard.rename(
        columns = {
            leaderboard.columns[1]: "NOW",
            leaderboard.columns[-2]: "PAST"
        },
        inplace = True
    )
    
    return dict(
        error = None,
        content = leaderboard
    )