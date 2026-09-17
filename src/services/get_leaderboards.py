from datetime import datetime
from src.data_collection.data_maps import DictMap
from src.data_collection.parsers.make_leaderboard import make_leaderboard
from src.data_collection.parsers.make_winloss import make_winloss

def get_leaderboards(
    timestamp: datetime.datetime,
    leaderboard_urls_dict: dict,
    winloss_url: str | None = None
) -> DictMap:
    leaderboards_dict = dict()

    if winloss_url:
        wl_map = make_winloss(winloss_url)

        if wl_map["error"]:
            return dict(
                error = wl_map["error"],
                content = None
            )

        winloss = wl_map["content"]
        
        leaderboards_dict["winloss"] = winloss

    for leaderboard_key, leaderboard_url in leaderboard_urls_dict.items():
        leaderboard_map = make_leaderboard(
            leaderboard_url = leaderboard_url,
            timestamp = timestamp
        )

        if leaderboard_map["error"]:
            return dict(
                error = leaderboard_map["error"],
                content = None
            )

        leaderboard = leaderboard_map["content"]

        leaderboards_dict[leaderboard_key] = leaderboard

    return dict(
        error = None,
        content = leaderboards_dict
    )