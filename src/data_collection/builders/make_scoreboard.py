from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_match_results import scan_match_results

def make_scoreboard(url: str) -> DataFrameMap:
    scoreboard_map = scan_match_results(url)

    if scoreboard_map["error"]:
        return DataFrameMap(
            error=scoreboard_map["error"],
            content=None
        )

    scoreboard = scoreboard_map["content"]

    scoreboard.rename(
        columns={
            "T": "SCORE"
        },
        inplace=True
    )

    scoreboard["SCORE"] = scoreboard["SCORE"].astype(float)

    scoreboard = scoreboard[["TEAM NAME", "SCORE"]]

    return DataFrameMap(
        error=None,
        content=scoreboard
    )