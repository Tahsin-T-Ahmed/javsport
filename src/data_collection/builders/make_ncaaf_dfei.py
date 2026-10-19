from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_ncaaf_dfei import scan_ncaaf_dfei

def make_ncaaf_dfei(url: str) -> DataFrameMap:
    dfei_map = scan_ncaaf_dfei(url)

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