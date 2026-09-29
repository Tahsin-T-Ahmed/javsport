from datetime import datetime
from src.data_collection.data_maps import DictMap
from src.data_collection.builders.make_leaderboard import make_leaderboard
from src.data_collection.builders.make_win_trends import make_win_trends
from streamlit.delta_generator import DeltaGenerator

def get_leaderboards(
    timestamp: datetime.datetime,
    leaderboard_urls_dict: dict,
    sport_title: str,
    progress_bar: DeltaGenerator | None = None,
    win_trends_url: str | None = None
) -> DictMap:
    loading_progress = 0
    leaderboards_dict = dict()

    n_leaderboards = len(leaderboard_urls_dict)

    if win_trends_url:
        n_leaderboards += 1

    if win_trends_url:
        wl_map = make_win_trends(win_trends_url)

        if wl_map["error"]:
            return DictMap(
                error=wl_map["error"],
                content=None
            )

        win_trends = wl_map["content"]

        if progress_bar:        
            progress_bar.progress(
                value = loading_progress/n_leaderboards,
                text=f"Loading {sport_title} Win-Trends..."
            )

        leaderboards_dict["win_trends"] = win_trends
        loading_progress += 1

    for leaderboard_key, leaderboard_url in leaderboard_urls_dict.items():
        if progress_bar:
            progress_bar.progress(
                value=loading_progress/n_leaderboards,
                text=f"Loading {sport_title} {' '.join([word.capitalize() for word in leaderboard_key.split('_')])}..."
            )

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
        loading_progress += 1

        leaderboards_dict[leaderboard_key] = leaderboard

    progress_bar.progress(
        value=1.0,
        text=f"Leaderboards Loaded!"
    )

    return DictMap(
        error=None,
        content=leaderboards_dict
    )