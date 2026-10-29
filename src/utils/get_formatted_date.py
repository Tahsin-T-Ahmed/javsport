import datetime
from src.utils.get_date_ordinal_suffix import get_date_ordinal_suffix

def get_formatted_date(timestamp: datetime.datetime) -> str:
    
    year = timestamp.year
    month = timestamp.strftime('%B')
    day = timestamp.day
    weekday = timestamp.strftime("%A")
    day_ordinal_suffix = get_date_ordinal_suffix(day)

    date_f = f"{weekday}, {month} {day}{day_ordinal_suffix}, {year}"

    return date_f