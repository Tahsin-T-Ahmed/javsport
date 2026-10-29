from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers.scan_ftnfantasy_table import scan_ftnfantasy_table
from streamlit.typing import UploadedFile

def make_nfl_dave(
    file: UploadedFile
) -> DataFrameMap:
    table_map = scan_ftnfantasy_table(file)

    if table_map["error"]:
        return DataFrameMap(
            error=table_map["error"],
            content=None
        )

    table = table_map["content"]

    table = table[["TEAM", "OFF DAVE", "DEF DAVE"]]

    return DataFrameMap(
        error=None,
        content=table
    )