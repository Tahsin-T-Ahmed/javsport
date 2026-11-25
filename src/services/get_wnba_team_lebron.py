from src.data_collection.builders.make_wnba_team_lebron import make_wnba_team_lebron
from src.data_collection.data_maps import DataFrameMap
from streamlit.typing import UploadedFile

def get_wnba_team_lebron(
    file: UploadedFile
) -> DataFrameMap:
    lebron_map = make_wnba_team_lebron(file)

    if lebron_map["error"]:
        return DataFrameMap(
            error=lebron_map["error"],
            content=None
        )

    lebron_df = lebron_map["content"]

    return DataFrameMap(
        error=None,
        content=lebron_df
    )