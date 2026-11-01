from src.data_collection.builders.make_tr_win_trends import make_tr_win_trends
from src.data_collection.data_maps import DataFrameMap

def get_win_trends(
    url: str
) -> DataFrameMap:
    wintrends_map = make_tr_win_trends(record_url=url)

    if wintrends_map["error"]:
        return DataFrameMap(
            error=wintrends_map["error"],
            content=None
        )

    win_trends = wintrends_map["content"]

    return DataFrameMap(
        error=None,
        content=win_trends
    )