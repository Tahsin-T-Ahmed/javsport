from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_cfb_table import scan_cfb_table

def make_cfb_leaderboard(url: str) -> DataFrameMap:
    leaderboard_map = scan_cfb_table(url)
    
    if leaderboard_map["error"]:
        return DataFrameMap(
            error=leaderboard_map["error"],
            content=None
        )

    leaderboard = leaderboard_map["content"]

    leaderboard.rename(
        columns={
            "Name": "TEAM CFB NAME",
            "Total/G": "PER GAME"
        },
        inplace=True
    )

    leaderboard = leaderboard[["TEAM CFB NAME", "PER GAME"]]

    return DataFrameMap(
        error=None,
        content=leaderboard
    )