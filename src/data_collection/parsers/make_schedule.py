import datetime
import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_table_at_date import scan_table_at_date
from src.data_collection.parsers.parse_teams import parse_teams

def make_schedule(
    schedule_url: str,
    timestamp: datetime.datetime
) -> DataFrameMap:
    year, month, day = f"{timestamp.year:04d}", f"{timestamp.month:02d}", f"{timestamp.day:02d}"
    date_str = f"{year}-{month}-{day}"

    schedule_map = scan_table_at_date(
        url=schedule_url,
        timestamp=timestamp
    )
    if schedule_map["error"]:
        return DataFrameMap(
            error=schedule_map["error"],
            content=None
        )

    schedule = schedule_map["content"]

    if schedule.empty:
        return DataFrameMap(
            error=None,
            content=schedule
        )

    schedule["TIME"] = schedule["TIME"].apply(lambda row: f"{date_str} {row}")
    schedule["TIME"] = pd.to_datetime(schedule["TIME"])

    schedule["TEAMS PARSED"] = schedule["TITLE"].apply(
        lambda col: parse_teams(col)["content"]
    )

    schedule[["TEAM A", "TEAM B"]] = schedule["TEAMS PARSED"].str.split("-", expand=True)

    schedule = schedule[["TITLE", "TIME", "TEAM A", "TEAM B"]]

    schedule["TEAM B IS HOME"] = schedule.apply(
        func=lambda row: True if "@" in row["TITLE"] or " at " in row["TITLE"] else False,
        axis=1
    )

    return DataFrameMap(
        error=None,
        content=schedule
    )