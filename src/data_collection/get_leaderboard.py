from src.data_collection.get_soup import get_soup
import pandas as pd
from src.data_collection.data_maps import DataFrameMap

def get_leaderboard(leaderboard_url:str, read_datasort:bool = False) -> DataFrameMap:
    soup_map = get_soup(leaderboard_url)
    if soup_map["error"]:
        return dict(
            error = soup_map["error"],
            content = None
        )

    soup = soup_map["content"]

    headers_raw = soup.find_all("th")
    if not headers_raw:
        return dict(
            error = f"ERROR (Leaderboard): Failed to scan HEADERS from URL ({leaderboard_url})",
            content = None
        )
    headers = [header.text.upper() for header in headers_raw]

    rows = soup.find_all("tr")
    if not rows:
        return dict(
            error = f"ERROR (Leaderboard): Failed to scan ROWS from URL ({leaderboard_url})",
            content = None
        )
    
    headers[-1] = "PAST"
    
    df = pd.DataFrame(columns = headers)

    for i, row in enumerate(rows):
        if 0 == i:
            continue

        cells = row.find_all("td")
        if not cells:
            return dict(
                error = f"ERROR (Leaderboard): Failed to scan CELLS of row ({row}) from URL ({leaderboard_url})",
                content = False
            )

        new_row_idx = df.shape[0]

        for col_idx, col in enumerate(headers):
            cell = cells[col_idx]
            cell_content = cell.text

            if headers.index("TEAM") == col_idx:
                team_link = cell.find("a")
                if not team_link:
                    return dict(
                        error = f"ERROR (Leaderboard): Failed to scan TEAM-LINK of cell ({cell}) from URL ({leaderboard_url})",
                        content = None
                    )
                
                cell_content = team_link["href"].split("/")[-1]
            else:
                if read_datasort:
                    cell_content = cell["data-sort"]

            df.loc[new_row_idx, col] = cell_content.strip()

    df.rename(
        columns = {
            "TEAM": "TEAM ID",
            df.columns[2]: "NOW"
        }, 
        inplace = True
    )
    
    return dict(
        error = None,
        content = df
    )