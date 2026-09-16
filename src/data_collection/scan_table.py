from bs4 import BeautifulSoup
import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.get_soup import get_soup

def scan_table(url:str) -> DataFrameMap:
    soup_map = get_soup(url)
    if soup_map["error"]:
        return dict(
            error = soup_map["error"],
            content = None
        )

    soup = soup_map["content"]

    datatable = soup.select("table.datatable")[0]
    if not datatable:
        return dict(
            error = f"ERROR (Table-Scan): Failed to scan DATATABLE from URL ({url})",
            content = None
        )

    headers = datatable.find_all("th")
    if not headers:
        return dict(
            error = f"Error (Table-Scan): Failed to scan HEADERS from URL ({url})",
            content = None
        )

    columns = [header.text.upper() for header in headers]

    table = pd.DataFrame(columns = columns)

    rows = datatable.find_all("tr")
    if not rows:
        return dict(
            error = f"ERROR (Table-Scan): Failed to scan ROWS from URL ({url})",
            content = None
        )

    for row_idx, row in enumerate(rows):
        if 0 == row_idx:
            continue

        cells = row.find_all("td")
        if not cells:
            return dict(
                error = f"ERROR (Table-Scan): Failed to scan CELLS of row ({row}) from URL ({url})",
                content = None
            )

        new_row_idx = table.shape[0]

        for column_idx, column in enumerate(columns):
            cell = cells[column_idx]

            table.loc[new_row_idx, column] = cell.text.strip()

            if cell.has_attr("data-sort"):
                table.loc[new_row_idx, f"{column}_DATASORT"] = cell["data-sort"].strip()
            
            cell_link = cell.find("a")
            if cell_link:
                table.loc[new_row_idx, f"{column}_LINK"] = cell_link["href"].strip()

    return dict(
        error = None,
        content = table
    )