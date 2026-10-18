import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.get_soup import get_soup

def scan_ncaaf_dfei(url: str) -> DataFrameMap:
    soup_map = get_soup(url)

    if soup_map["error"]:
        return DataFrameMap(
            error=soup_map["error"],
            content=None
        )

    soup = soup_map["content"]

    dfei_df = pd.DataFrame()

    rows = soup.find_all("tr")
    if not rows:
        return DataFrameMap(
            error=f"ERROR (DFEI-Scanner): Failed to scan ROWS from URL ({url})",
            content=None
        )

    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue

        if len(cells) < 5:
            continue

        if "TEAM" == cells[1].text.strip().upper():
            continue

        new_row_idx = dfei_df.shape[0]

        dfei_df.loc[new_row_idx, "TEAM NAME"] = cells[1].text
        dfei_df.loc[new_row_idx, "DFEI"] = cells[4].text

    return DataFrameMap(
        error=None,
        content=dfei_df
    )