from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_table import scan_table

def make_win_trends(record_url: str) -> DataFrameMap:
    wintrends_map = scan_table(record_url)
    if wintrends_map["error"]:
        return DataFrameMap(
            error=wintrends_map["error"],
            content=None
        )

    win_trends = wintrends_map["content"]

    win_trends.rename(
        columns={
            "WIN %_DATASORT": "WIN RATE"
        },
        inplace=True
    )

    win_trends[["WINS", "LOSSES", "TIES"]] = win_trends["WIN-LOSS RECORD"].str.split("-", expand=True)

    desired_columns = ["TEAM", "WINS", "LOSSES", "TIES", "WIN RATE"]
    win_trends = win_trends[desired_columns]

    return DataFrameMap(
        error=None,
        content=win_trends
    )