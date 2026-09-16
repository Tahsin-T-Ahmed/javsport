from src.data_collection.get_soup import get_soup
import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def get_schedule(schedule_url:str) -> DataFrameMap:
    soup_map = get_soup(schedule_url)
    if soup_map["error"]:
        return dict(
            error = soup_map["error"],
            content = None
        )

    soup = soup_map["content"]

    headers_raw = soup.find_all("th")
    if not headers_raw:
        return dict(
            error = f"ERROR (Schedule): Failed to scan HEADERS from URL ({schedule_url})",
            content = None
        )    
    headers = [cell.text.upper() for cell in headers_raw]

    rows = soup.find_all("tr")
    if not rows:
        return dict(
            error = f"ERROR (Schedule): Failed to scan ROWS from URL ({schedule_url})",
            content = None
        )

    headers[1] = "HOTNESS"

    df = pd.DataFrame(columns = headers)

    for row_idx, row in enumerate(rows):
        if 0 == row_idx:
            continue

        cells = row.find_all("td")
        if not cells:
            return dict(
                error = f"ERROR (Schedule): Failed to scan CELLS from URL ({schedule_url})",
                content = None
            )

        new_row_idx = df.shape[0]
        
        for header_idx, header in enumerate(headers):
            cell_content = cells[header_idx].text
            
            if "MATCHUP" == header:
                match_link = cells[header_idx].find("a")
                if not match_link:
                    return dict(
                        error = f"ERROR (Schedule): Failed to scan MATCH-LINK (#{header_idx+1}) of {cells[header_idx]} from URL ({schedule_url})",
                        content = None
                    )
                
                cell_content = match_link["href"].split("/")[-1]

            df.loc[new_row_idx, header] = cell_content.strip()

    df.rename(columns = {"MATCHUP": "MATCH ID"}, inplace = True)

    df["TIME"] = pd.to_datetime(df["TIME"])

    return dict(
        error = None,
        content = df
    )