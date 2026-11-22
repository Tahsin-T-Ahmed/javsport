from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers.scan_nba_team_xpm import scan_nba_team_xpm
from streamlit.typing import UploadedFile

def make_nba_team_xpm(
    file: UploadedFile
) -> DataFrameMap:
    xpm_map = scan_nba_team_xpm(file)

    if xpm_map["error"]:
        return DataFrameMap(
            error=xpm_map["error"],
            content=None
        )

    xpm_df = xpm_map["content"]

    xpm_df = xpm_df[[1, 3, 4, 5]]

    column_names = ["TEAM BBI NAME", "XPM OFFENSE", "XPM DEFENSE", "XPM NET"]

    xpm_df.columns = column_names

    return DataFrameMap(
        error=None,
        content=xpm_df
    )