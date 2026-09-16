from src.data_collection.get_leaderboard import get_leaderboard
import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def get_winloss(record_url:str) -> DataFrameMap:
    record_soup = get_leaderboard(record_url)
    if record_soup["error"]:
        return dict(
            error = record_soup["error"],
            content = None
        )

    record_raw = record_soup["content"]

    winloss_df = pd.DataFrame({
        "TEAM ID": record_raw["TEAM ID"]
    })

    winloss_df[["WINS", "LOSSES", "TIES"]] = record_raw["WIN-LOSS RECORD"].str.split("-", expand = True)

    return dict(
        error = None,
        content = winloss_df
    )