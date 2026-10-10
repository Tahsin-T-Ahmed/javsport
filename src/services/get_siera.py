from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers.scan_pitchers_data import scan_pitchers_data
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile

def get_siera(
    file: UploadedFile,
    progress_bar: DeltaGenerator | None = None,
    **kwargs
) -> DataFrameMap:
    table_map = scan_pitchers_data(
        file=file,
        progress_bar=progress_bar
    )

    if table_map["error"]:
        return DataFrameMap(
            error=table_map["error"],
            content=None
        )

    table = table_map["content"]

    if "SIERA" not in [column.upper() for column in table.columns]:
        return DataFrameMap(
            error=f"'SIERA' column not found",
            content=None
        )

    if progress_bar:
        progress_bar.status(
            label="SIERA Scan Complete! :green[:material/check:]",
            state="complete"
        )

    return DataFrameMap(
        error=None,
        content=table
    )