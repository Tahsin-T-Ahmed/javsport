from datetime import datetime
from src.data_collection.data_maps import DictMap
from src.data_collection.parsers.make_schedule import make_schedule
from src.services.get_leaderboards import get_leaderboards

def get_sport_data(
    timestamp: datetime.datetime,
    schedule_url: str,
    leaderboard_urls_dict: dict,
    win_trends_url: str | None = None
) -> DictMap:
    sport_data_dict = dict()

    schedule_map = make_schedule(
        schedule_url = schedule_url,
        timestamp = timestamp
    )

    if schedule_map["error"]:
        return dict(
            error = schedule_map["error"],
            content = None
        )

    schedule = schedule_map["content"]
    sport_data_dict["schedule"] = schedule

    if schedule.empty:
        return dict(
            error = None,
            content = sport_data_dict
        )

    schedule_display = schedule.copy()
    schedule_display["TIME"] = schedule_display["TIME"].dt.strftime("%I:%m %p")

    sport_data_dict["schedule_display"] = schedule_display
    
    leaderboards_map = get_leaderboards(
        timestamp = timestamp,
        leaderboard_urls_dict = leaderboard_urls_dict,
        win_trends_url = win_trends_url
    )

    if leaderboards_map["error"]:
        return dict(
            error = leaderboards_map["error"],
            content = None
        )

    leaderboards = leaderboards_map["content"]
    sport_data_dict["leaderboards"] = leaderboards

    return dict(
        error = None,
        content = sport_data_dict
    )