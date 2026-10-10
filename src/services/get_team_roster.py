from src.data_collection.builders.make_team_roster import make_team_roster
from src.data_collection.data_maps import DataFrameMap

def get_team_roster(url: str) -> DataFrameMap:
    roster_map = make_team_roster(url=url)

    if roster_map["error"]:
        return DataFrameMap(
            error=roster_map["error"],
            content=None
        )

    roster = roster_map["content"]

    roster = roster[["TEAM NAME", "TEAM TRID"]]

    roster.set_index(
        keys="TEAM TRID",
        inplace=True
    )

    return DataFrameMap(
        error=None,
        content=roster
    )