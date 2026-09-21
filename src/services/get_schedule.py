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
        return DictMap(
            error = schedule_raw_map["error"],
            content = None
        )

    schedule = schedule_raw_map["content"]
    schedule_dict["data"] = schedule

    if schedule.empty:
        return DictMap(
            error = None,
            content = schedule_dict
        )

    schedule_display = schedule.copy()
    schedule_display["TIME"] = schedule_display["TIME"].dt.strftime("%I:%M %p")
    schedule_display["HOME TEAM"] = schedule_display.apply(
        func = lambda row: row["TEAM B"] if row["TEAM B IS HOME"] else None,
        axis = 1
    )

    schedule_display.drop(columns=["TEAM B IS HOME"], inplace=True)

    schedule_dict["display"] = schedule_display

    return DictMap(
        error = None,
        content = schedule_dict
    )