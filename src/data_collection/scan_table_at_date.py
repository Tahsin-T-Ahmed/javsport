from datetime import datetime
import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.get_soup import get_soup

def scan_table_at_date(url: str, timestamp: datetime.datetime) -> DataFrameMap:
    soup_map = get_soup(url)
    if soup_map["error"]:
        return dict(
            error = soup_map["error"],
            conent = None
        )

    soup = soup_map["content"]

    date_str = f"{timestamp.strftime('%a %b')} {timestamp.day}"

    todays_cell = soup.find("th", string=date_str)
    if not todays_cell:
        return dict(
            error = None,
            content = pd.DataFrame()
        )

    head = todays_cell.parent.parent

    headers = head.find_all("th")

    columns = [header.text.strip().upper() for header in headers]
    columns[0] = "TITLE"

    body = head.find_next_sibling("tbody")
    if not body:
        return dict(
            error = f"ERROR (TableArray-Scan): Failed to scan BODY for head ({head}) from URL ({url})",
            content = None
        )

    rows = body.find_all("tr")
    if not rows:
        return dict(
            error = f"ERROR (TableArray-Scan): Failed to scan ROWS in body ({body}) from URL ({url})",
            content = None
        )

    table = pd.DataFrame(columns = columns)

    for row in rows:
        cells = row.find_all("td")
        if not cells:
            return dict(
                error = f"ERROR (TableArray-Scan): Failed to scan CELLS of row ({row}) from URL ({url})",
                content = None
            )

        new_row_idx = table.shape[0]

        for column_idx, column in enumerate(columns):
            cell = cells[column_idx]

            if cell.has_attr("class") and "empty" in cell["class"]:
                return dict(
                    error = None,
                    content = table
                )

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