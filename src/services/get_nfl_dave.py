from src.data_collection.data_maps import DataFrameMap
from src.data_collection.builders.make_nfl_dave import make_nfl_dave
from streamlit.typing import UploadedFile

def get_nfl_dave(
    file: UploadedFile,
    **kwargs
) -> DataFrameMap:
    dave_map = make_nfl_dave(file)

    if dave_map["error"]:
        return DataFrameMap(
            error=dave_map["error"],
            content=None
        )

    dave = dave_map["content"]

    return DataFrameMap(
        error=None,
        content=dave
    )