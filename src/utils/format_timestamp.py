from datetime import datetime
from src.utils.get_date_ordinal_suffix import get_date_ordinal_suffix

def format_timestamp(timestamp) -> dict:
    date = timestamp.strftime('%Y, %B %d')
    clocktime = timestamp.strftime('%I:%M:%S %p')
    timezone = timestamp.astimezone().tzname()
    ordinal_suffix = get_date_ordinal_suffix(timestamp.day)

    return {
        "date": f"{date}{ordinal_suffix}",
        "clocktime": clocktime,
        "timezone": timezone
    }