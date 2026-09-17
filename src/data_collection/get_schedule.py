import datetime
import pandas as pd
from src.data_collection.data_maps import DataFrameMap, ListMap
from src.data_collection.scan_todays_table import scan_todays_table

def parse_teams(title: str) -> ListMap:
    title_splitter = None
    if "@" in title:
        title_splitter = "@"
    elif "at" in title:
        title_splitter = "at"
    elif "vs." in title:
        title_splitter = "vs."
    elif "vs" in title:
        title_splitter = "vs"
    else:
        return dict(
            error = f"ERROR (Teams-Parser): No valid OPPONENT-INDICATOR found in match title ({title})",
            content = None
        )

    title_terms = title.split(title_splitter)

    teams = [term.strip() for term in title_terms]

    return '-'.join(teams)


def get_schedule(schedule_url: str, timestamp: datetime.datetime) -> DataFrameMap:
    year, month, day = f"{timestamp.year:04d}", f"{timestamp.month:02d}", f"{timestamp.day:02d}"
    date_str = f"{year}-{month}-{day}"

    schedule_map = scan_todays_table(
        url = schedule_url,
        timestamp = timestamp
    )
    if schedule_map["error"]:
        return dict(
            error = schedule_map["error"],
            content = None
        )

    schedule = schedule_map["content"]

    if schedule.empty:
        return dict(
            error = None,
            content = schedule
        )

    schedule["TIME"] = schedule["TIME"].apply(lambda row: f"{date_str} {row}")
    schedule["TIME"] = pd.to_datetime(schedule["TIME"])

    schedule[["TEAM A", "TEAM B"]] = schedule["TITLE"].apply(parse_teams).str.split("-", expand = True)

    schedule = schedule[["TITLE", "TIME", "TEAM A", "TEAM B"]]

    return dict(
        error = None,
        content = schedule
    )