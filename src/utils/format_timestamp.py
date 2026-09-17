from datetime import datetime

def format(timestamp):
    date = timestamp.strftime('%Y, %B %d')
    clocktime = timestamp.strftime('%I:%M:%S %p')
    timezone = timestamp.astimezone().tzname()
    
    ordinal_suffix = None
    day_of_month = timestamp.day

    match(timestamp.day):
        case 1 | 21: 
            ordinal_suffix = "st"
        case 2 | 22:
            ordinal_suffix = "nd"
        case 3 | 23:
            ordinal_suffix = "rd"
        case _:
            ordinal_suffix = "th"

    return {
        "date": f"{date}{ordinal_suffix}",
        "clocktime": clocktime,
        "timezone": timezone
    }