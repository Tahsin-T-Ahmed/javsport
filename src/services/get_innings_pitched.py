import datetime
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers.scan_pitchers_data import scan_pitchers_data
from streamlit.typing import UploadedFile

def get_innings_pitched(
    file: UploadedFile,
    timestamp: datetime.datetime
) -> DataFrameMap:
    table_map = scan_pitchers_data(
        file=file,
        timestamp=timestamp
    )

    if table_map["error"]:
        return DataFrameMap(
            error=table_map["error"],
            content=None
        )

    table = table_map["content"]

    if "IP" not in [column.upper() for column in table.columns]:
        return DataFrameMap(
            error=f"'IP' column not found",
            content=None
        )

    return DataFrameMap(
        error=None,
        content=table
    )