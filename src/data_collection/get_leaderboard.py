from datetime import datetime
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scan_table import scan_table

def get_leaderboard(leaderboard_url: str, timestamp: datetime.datetime) -> DataFrameMap:
    year, month, day = f"{timestamp.year:04d}", f"{timestamp.month:02d}", f"{timestamp.day:02d}"
    date_str = f"{year}-{month}-{day}"

    leaderboard_map = scan_table(f"{leaderboard_url}?date={date_str}")
    if leaderboard_map["error"]:
        return dict(
            error = leaderboard_map["error"],
            content = None
        )

    leaderboard = leaderboard_map["content"]

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
            leaderboard.columns[-1]: "PAST"
        },
        inplace = True
    )
    
    return dict(
        error = None,
        content = leaderboard
    )