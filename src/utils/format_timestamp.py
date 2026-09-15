from datetime import datetime

def format(timestamp):
    date = timestamp.strftime('%Y, %B %d')
    clocktime = timestamp.strftime('%I:%M:%S %p')
    timezone = timestamp.astimezone().tzname()

    return {
        "date": date,
        "clocktime": clocktime,
        "timezone": timezone
    }