from src.data_collection.get_leaderboard import get_leaderboard
import pandas as pd

def get_winloss(url:str) -> pd.DataFrame:
    lb_raw = get_leaderboard(url)
    # if not lb_raw:
    #     return

    lb = pd.DataFrame({
        "TEAM ID": lb_raw["TEAM ID"]
    })

    lb[["WINS", "LOSSES", "TIES"]] = lb_raw["WIN-LOSS RECORD"].str.split("-", expand = True)

    return lb