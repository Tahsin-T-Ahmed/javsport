import pandas as pd
from src.data_collection.scrapers.get_soup import get_soup
from src.data_collection.data_maps import DataFrameMap

def scan_cfbstats_table(url: str) -> DataFrameMap:
    soup_map = get_soup(url)

    if soup_map["error"]:
        return DataFrameMap(
            error=soup_map["error"],
            content=None
        )

    soup = soup_map["content"]

    rows = soup.find_all("tr")
    if not rows:
        return DataFrameMap(
            error=f"ERROR (CFB Table-Scanner): Failed to scan ROWS from URL ({url})",
            content=None
        )

    headers = rows[0].find_all("th")
    columns = [header.text for header in headers]

    cfb_table = pd.DataFrame(columns=columns)

    for row_idx, row in enumerate(rows):
        cells = row.find_all("td")
        if not cells:
            continue

        new_row_idx = cfb_table.shape[0]

        cfb_table.loc[new_row_idx, :] = [str(cell.text) for cell in cells]

    return DataFrameMap(
        error=None,
        content=cfb_table
    )