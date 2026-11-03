from datetime import datetime
from src.data_collection.data_maps import DictMap
from src.data_collection.builders.make_schedule import make_schedule

def get_schedule(
    timestamp: datetime.datetime,
    schedule_url: str
) -> DictMap:
    schedule_raw_map = make_schedule(
        schedule_url=schedule_url,
        timestamp=timestamp
    )

    if schedule_raw_map["error"]:
        return DictMap(
            error=schedule_raw_map["error"],
            content=None
        )

    schedule = schedule_raw_map["content"]

    if schedule.empty:
        return DictMap(
            error=None,
            content=schedule_dict
        )

    schedule.rename(
        columns={
            "TITLE_LINK": "MATCH URL"
        },
        inplace=True
    )

    schedule_display = schedule.copy()
    schedule_display["TIME"] = schedule_display["TIME"].dt.strftime("%I:%M %p")
    schedule_display["HOME TEAM"] = schedule_display.apply(
        func=lambda row: row["TEAM B"] if row["TEAM B IS HOME"] else None,
        axis=1
    )

    schedule_display = schedule_display[["TIME", "TEAM A", "TEAM B", "HOME TEAM"]]

    schedule_dict = dict(
        data=schedule,
        display=schedule_display
    )

    return DictMap(
        error=None,
        content=schedule_dict
    )