from get_soup import get_soup
import pandas as pd

def get_schedule(url:str) -> pd.DataFrame:
    soup = get_soup(url)
    if not soup:
        return

    headers_raw = soup.find_all("th")
    if not headers_raw:
        return
    
    headers = [cell.text.upper() for cell in headers_raw]

    rows = soup.find_all("tr")
    if not rows:
        return

    headers[1] = "HOTNESS"

    df = pd.DataFrame(columns = headers)

    for i, row in enumerate(rows):
        if 0 == i:
            continue

        cells = row.find_all("td")
        if not cells:
            return

        new_row_idx = df.shape[0]
        
        for idx, header in enumerate(headers):
            content = cells[idx].text
            
            if "MATCHUP" == header:
                match_link = cells[idx].find("a")
                if not match_link:
                    return
                
                content = match_link["href"].split("/")[-1]

            df.loc[new_row_idx, header] = content.strip()
            
    df.rename(columns = {"MATCHUP": "MATCH ID"}, inplace = True)

    df["TIME"] = pd.to_datetime(df["TIME"])
    return df