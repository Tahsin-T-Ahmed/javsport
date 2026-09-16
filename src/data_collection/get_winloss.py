from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scan_table import scan_table

def get_winloss(record_url: str) -> DataFrameMap:
    winloss_map = scan_table(record_url)
    if winloss_map["error"]:
        return dict(
            error = winloss_map["error"],
            content = None
        )

    winloss = winloss_map["content"]

    winloss["TEAM ID"] = winloss["TEAM_LINK"].apply(
        lambda link: link.split("/")[-1]
    )

    winloss.rename(
        columns = {
            "WIN %_DATASORT": "WIN RATE"
        },
        inplace = True
    )

    winloss[["WINS", "LOSSES", "TIES"]] = winloss["WIN-LOSS RECORD"].str.split("-", expand = True)

    desired_columns = ["TEAM", "WINS", "LOSSES", "TIES", "WIN RATE", "TEAM ID"]
    winloss = winloss[desired_columns]

    return dict(
        error = None,
        content = winloss
    )