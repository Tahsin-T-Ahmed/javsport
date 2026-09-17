from datetime import datetime
from src.utils.get_date_ordinal_suffix import get_date_ordinal_suffix

def format_timestamp(timestamp) -> dict:
    year = f"{timestamp.year:04d}"
    month_name = timestamp.strftime("%B")
    day = timestamp.day

    date_str = f"{year}, {month_name} {day}"
    clocktime = timestamp.strftime('%I:%M:%S %p')
    timezone = timestamp.astimezone().tzname()
    ordinal_suffix = get_date_ordinal_suffix(timestamp.day)

    return {
        "date": f"{date_str}{ordinal_suffix}",
        "clocktime": clocktime,
        "timezone": timezone
    }