from datetime import datetime
from src.data_collection.data_maps import DictMap
from src.data_collection.parsers.make_schedule import make_schedule

def get_schedule(
    timestamp: datetime.datetime,
    schedule_url: str
) -> DictMap:
    schedule_dict = dict()

    schedule_raw_map = make_schedule(
        schedule_url = schedule_url,
        timestamp = timestamp
    )

    if schedule_raw_map["error"]:
        return dict(
            error = schedule_raw_map["error"],
            content = None
        )

    schedule = schedule_raw_map["content"]
    schedule_dict["data"] = schedule

    if schedule.empty:
        return dict(
            error = None,
            content = schedule_dict
        )

    schedule_display = schedule.copy()
    schedule_display["TIME"] = schedule_display["TIME"].dt.strftime("%I:%m %p")

    schedule_dict["display"] = schedule_display

    return dict(
        error = None,
        content = schedule_dict
    )