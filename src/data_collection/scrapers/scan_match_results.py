import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scrapers.get_soup import get_soup

def scan_match_results(
    url: str
) -> DataFrameMap:
    url = f"{url}/box-score"
    
    soup_map = get_soup(url)

    if soup_map["error"]:
        return DataFrameMap(
            error=soup_map["error"],
            content=None
        )

    soup = soup_map["content"]

    table = soup.find("table")
    if not table:
        return DataFrameMap(
            error=f"ERROR (Match-Results-Scanner): Failed to scan TABLE from URL {url}",
            content=None
        )

    headers = [header.text.strip().upper() for header in table.find_all("th")]
    if not headers:
        return DataFrameMap(
            error=f"ERROR (Match-Results-Scanner): Failed to scan Table HEADERS from URL {url}",
            content=None
        )

    rows = table.find("tbody").find_all("tr")
    if not rows:
        return DataFrameMap(
            error=f"ERROR (Match-Results-Scanner): Failed to scan Table ROWS from URL {url}",
            content=None
        )

    match_results = pd.DataFrame()

    for row_idx, row in enumerate(rows):
        cells = row.find_all("td")
        if not cells:
            return DataFrameMap(
                error=f"ERROR (Match-Results-Scanner): Failed to scan CELLS of row from URL {url}",
                content=None
            )

        for header, cell in zip(headers, cells):
            match_results.loc[row_idx, header] = cell.text.strip()

    return DataFrameMap(
        error=None,
        content=match_results
    )