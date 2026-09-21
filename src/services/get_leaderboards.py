from datetime import datetime
from src.data_collection.data_maps import DictMap
from src.data_collection.parsers.make_leaderboard import make_leaderboard
from src.data_collection.parsers.make_win_trends import make_win_trends

def get_leaderboards(
    timestamp: datetime.datetime,
    leaderboard_urls_dict: dict,
    win_trends_url: str | None = None
) -> DictMap:
    leaderboards_dict = dict()

    if win_trends_url:
        wl_map = make_win_trends(win_trends_url)

        if wl_map["error"]:
            return DictMap(
                error=wl_map["error"],
                content=None
            )

        win_trends = wl_map["content"]
        
        leaderboards_dict["win_trends"] = win_trends

    for leaderboard_key, leaderboard_url in leaderboard_urls_dict.items():
        leaderboard_map = make_leaderboard(
            leaderboard_url=leaderboard_url,
            timestamp=timestamp
        )

        if leaderboard_map["error"]:
            return DictMap(
                error=leaderboard_map["error"],
                content=None
            )

        leaderboard = leaderboard_map["content"]

        leaderboards_dict[leaderboard_key] = leaderboard

    return DictMap(
        error=None,
        content=leaderboards_dict
    )