from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_tr_table import scan_tr_table

def make_winner_picks(
    url: str,
    month: int | str,
    day: int | str
) -> DataFrameMap:
    winner_picks_map = scan_tr_table(url=url)

    if winner_picks_map["error"]:
        return DataFrameMap(
            error=winner_picks_map["error"],
            content=None
        )

    winner_picks = winner_picks_map["content"]

    necessary_columns = ["DAY", "STATUS", "TR PICK", "OPP/GAME"]

    for column in necessary_columns:
        if not any(winner_picks.columns.str.contains(column)):
            return DataFrameMap(
                error=f"No '{column}' column at webpage {url}",
                content=None
            )

    winner_picks.rename(
        columns={
            "DAY": "DATE",
            "OPP/GAME": "OPPONENT"
        },
        inplace=True
    )

    winner_picks["OPPONENT"] = winner_picks["OPPONENT"].apply(
        lambda text: " ".join(text.split(" ")[1:])
    )

    winner_picks = winner_picks[["DATE", "STATUS", "TR PICK", "OPPONENT"]]

    return DataFrameMap(
        error=None,
        content=winner_picks
    )