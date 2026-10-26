import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.get_soup import get_soup

def scan_bcftoys_table(url: str) -> DataFrameMap:
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
            error=f"ERROR (BCFTOYS-Scanner): Failed to scan ROWS from URL ({url})",
            content=None
        )    

    columns = None

    bcf_table = None

    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue

        if len(cells) < 5:
            continue

        if "TEAM" == cells[1].text.strip().upper():
            if columns:
                continue

            columns = [cell.text for cell in cells]
            bcf_table = pd.DataFrame(columns=columns)
            continue

        new_row_idx = bcf_table.shape[0]

        bcf_table.loc[new_row_idx, :] = [str(cell.text) for cell in cells]

    bcf_table = bcf_table.loc[:, ~bcf_table.columns.duplicated(keep=False)]

    return DataFrameMap(
        error=None,
        content=bcf_table
    )