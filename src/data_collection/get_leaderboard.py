from src.data_collection.get_soup import get_soup
import pandas as pd

def get_leaderboard(url:str, read_datasort:bool = False) -> pd.DataFrame:
    soup = get_soup(url)
    if not soup:
        return

    headers_raw = soup.find_all("th")
    headers = [header.text.upper() for header in headers_raw]

    rows = soup.find_all("tr")
    if not rows:
        return
    
    headers[-1] = "PAST"
    
    df = pd.DataFrame(columns = headers)

    for i, row in enumerate(rows):
        if 0 == i:
            continue

        cells = row.find_all("td")
        if not cells:
            return

        new_row_idx = df.shape[0]

        for idx, col in enumerate(headers):
            content = cells[idx].text
            if headers.index("TEAM") == idx:
                team_link = cells[idx].find("a")
                if not team_link:
                    return
                
                content = team_link["href"].split("/")[-1]
            else:
                if read_datasort:
                    content = cells[idx]["data-sort"]

            df.loc[new_row_idx, col] = content.strip()

    df.rename(
        columns = {
            "TEAM": "TEAM ID",
            df.columns[2]: "NOW"
        }, 
        inplace = True
    )
    return df