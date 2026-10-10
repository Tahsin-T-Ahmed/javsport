from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_table import scan_table

def make_team_roster(url: str) -> DataFrameMap:
    table_map = scan_table(url=url)

    if table_map["error"]:
        return DataFrameMap(
            error=table_map["error"],
            content=None
        )

    roster = table_map["content"]

    roster["TEAM TRID"] = roster["TEAM_LINK"].apply(
        lambda link: link.split("/")[-1]
    )

    roster.rename(
        columns={
            "TEAM": "TEAM NAME"
        },
        inplace=True
    )

    return DataFrameMap(
        error=None,
        content=roster
    )