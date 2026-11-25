from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers.scan_wnba_team_lebron import scan_wnba_team_lebron
from streamlit.typing import UploadedFile

def make_wnba_team_lebron(
    file: UploadedFile
) -> DataFrameMap:
    lebron_map = scan_wnba_team_lebron(file)

    if lebron_map["error"]:
        return DataFrameMap(
            error=lebron_map["error"],
            content=None
        )

    lebron_df = lebron_map["content"]

    lebron_df = lebron_df[[1, 3, 4, 5]]

    lebron_df.columns = ["TEAM BBI NAME", "LEBRON OFFENSE", "LEBRON DEFENSE", "LEBRON NET"]

    return DataFrameMap(
        error=None,
        content=lebron_df
    )