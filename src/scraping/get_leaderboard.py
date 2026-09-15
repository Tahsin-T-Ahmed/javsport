import get_soup
import pandas as pd

def get_leaderboard(url:str, read_datasort:bool = False) -> pd.DataFrame:
    soup = get_soup(url)
    headers = [cell.text.upper() for cell in soup.find_all("th")]
    rows = soup.find_all("tr")
    
    headers[-1] = "PAST"
    
    df = pd.DataFrame(columns = headers)

    for i, row in enumerate(rows):
        if 0 == i:
            continue

        cells = row.find_all("td")

        new_row_idx = df.shape[0]

        for idx, col in enumerate(headers):
            content = cells[idx].text
            if headers.index("TEAM") == idx:
                content = cells[idx].find("a")["href"].split("/")[-1]
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