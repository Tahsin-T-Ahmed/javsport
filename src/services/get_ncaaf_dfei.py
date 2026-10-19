from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_bcftoys_table import scan_bcftoys_table

def get_ncaaf_dfei(url: str) -> DataFrameMap:
    dfei_map = scan_bcftoys_table(url)

    if dfei_map["error"]:
        return DataFrameMap(
            error=dfei_map["error"],
            content=None
        )

    dfei_df = dfei_map["content"]

    return DataFrameMap(
        error=None,
        content=dfei_df
    )