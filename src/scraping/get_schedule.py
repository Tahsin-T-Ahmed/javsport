import get_soup
import pandas as pd

def get_schedule(url:str) -> pd.DataFrame:
    soup = get_soup(url)
    headers = [cell.text.upper() for cell in soup.find_all("th")]
    rows = soup.find_all("tr")

    headers[1] = "HOTNESS"

    df = pd.DataFrame(columns = headers)

    for i, row in enumerate(rows):
        if 0 == i:
            continue

        cells = row.find_all("td")

        new_row_idx = df.shape[0]
        
        for idx, header in enumerate(headers):
            content = cells[idx].text
            if "MATCHUP" == header:
                content = cells[idx].find("a")["href"].split("/")[-1]
                # df.loc[new_row_idx, ["TEAM A", "TEAM B"]] = get_teams(content)

            df.loc[new_row_idx, header] = content.strip()
            
    df.rename(columns = {"MATCHUP": "MATCH ID"}, inplace = True)

    df["TIME"] = pd.to_datetime(df["TIME"])
    return df