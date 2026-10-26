from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.scan_bcftoys_table import scan_bcftoys_table

def get_ncaaf_ofei(url: str) -> DataFrameMap:
    ofei_map = scan_bcftoys_table(url)

    if ofei_map["error"]:
        return DataFrameMap(
            error=ofei_map["error"],
            content=None
        )

    ofei_df = ofei_map["content"]

    ofei_df.rename(
        columns={
            "Team": "TEAM BCF NAME"
        },
        inplace=True
    )

    ofei_df = ofei_df[["TEAM BCF NAME", "OFEI"]]

    return DataFrameMap(
        error=None,
        content=ofei_df
    )