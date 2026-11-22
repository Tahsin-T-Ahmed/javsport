from src.data_collection.builders.make_nba_team_xpm import make_nba_team_xpm
from src.data_collection.data_maps import DataFrameMap
from streamlit.typing import UploadedFile

def get_nba_team_xpm(
    file: UploadedFile,
    **kwargs
) -> DataFrameMap:
    xpm_map = make_nba_team_xpm(file)

    if xpm_map["error"]:
        return DataFrameMap(
            error=xpm_map["error"],
            content=None
        )

    xpm = xpm_map["content"]

    return DataFrameMap(
        error=None,
        content=xpm
    )