from datetime import datetime
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_table import scan_table

def make_leaderboard(
    leaderboard_url: str,
    timestamp: datetime.datetime
) -> DataFrameMap:
    year, month, day = f"{timestamp.year:04d}", f"{timestamp.month:02d}", f"{timestamp.day:02d}"
    date_str = f"{year}-{month}-{day}"

    leaderboard_map = scan_table(f"{leaderboard_url}?date={date_str}")
    if leaderboard_map["error"]:
        return DataFrameMap(
            error=leaderboard_map["error"],
            content=None
        )

    leaderboard = leaderboard_map["content"]

    leaderboard = leaderboard[[col for col in leaderboard.columns if "_DATASORT" in col]]

    leaderboard.columns = [column.replace("_DATASORT", "") for column in leaderboard.columns]

    leaderboard.drop(
        columns=["RANK", "LAST 3", "LAST 1"],
        inplace=True
    )

    year_cols = leaderboard.columns.drop(["TEAM", "HOME", "AWAY"])
    latest_season = max(year_cols)

    leaderboard = leaderboard[["TEAM", latest_season, "HOME", "AWAY"]]

    leaderboard.rename(
        columns={
            latest_season: "OVERALL"
        },
        inplace=True
    )

    numeric_columns = leaderboard.columns.drop("TEAM")
    leaderboard[numeric_columns] = leaderboard[numeric_columns].astype(float)
    
    return DataFrameMap(
        error=None,
        content=leaderboard
    )