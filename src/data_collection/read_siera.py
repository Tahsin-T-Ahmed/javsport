import io
import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def parse_text(siera_text:str) -> DataFrameMap:
    siera_table = pd.read_csv(
        io.StringIO(siera_text),
        sep = "\t",
        index_col = 0
    )

    return dict(
        error = None,
        content = siera_table
    )