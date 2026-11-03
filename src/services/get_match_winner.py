from src.data_collection.data_maps import StringMap
from src.data_collection.builders.make_scoreboard import make_scoreboard

def get_match_winner(url: str) -> StringMap:
    scoreboard_map = make_scoreboard(url)

    if scoreboard_map["error"]:
        return StringMap(
            error=scoreboard_map["error"],
            content=None
        )

    scoreboard = scoreboard_map["content"]

    if scoreboard["SCORE"].max() == scoreboard["SCORE"].min():
        return StringMap(
            error=None,
            content=None
        )

    winner = scoreboard.loc[scoreboard["SCORE"].idxmax(), "TEAM NAME"]

    return StringMap(
        error=None,
        content=winner
    )