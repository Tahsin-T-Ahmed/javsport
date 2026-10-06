from bs4 import BeautifulSoup
import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from streamlit.typing import UploadedFile
from unidecode import unidecode

def scan_mlb_probables(
    file: UploadedFile,
    **kwargs
) -> DataFrameMap:
    soup = BeautifulSoup(file)

    rows = soup.find_all("tr")
    if not rows:
        return DataFrameMap(
            error=f"ERROR (MLB Probables-Scanner): Failed to scan ROWS of page",
            content=None
        )

    probgrid = pd.DataFrame()

    for row_idx, row in enumerate(rows):
        cells = row.find_all("td")
        if not cells:
            continue

        if " " in cells[0].text:
            continue

        new_row_idx = probgrid.shape[0]

        pitcher_links = cells[1].find_all("a")
        if not pitcher_links:
            continue

        probgrid.loc[new_row_idx, "FG TEAM"] = cells[0].text
        probgrid.loc[new_row_idx, "N PITCHERS"] = len(pitcher_links)

        for pitcher_idx, pitcher_link in enumerate(pitcher_links):
            if not pitcher_link.has_attr("href"):
                continue

            pitcher_name = pitcher_link.text.split("(")[0].strip()
            probgrid.loc[new_row_idx, f"PITCHER {pitcher_idx+1}"] = unidecode(pitcher_name)

            pitcher_fgid = pitcher_link["href"].split("/stats")[0].split("/")[-1]

            probgrid.loc[new_row_idx, f"PITCHER {pitcher_idx+1} FGID"] = pitcher_fgid

    return DataFrameMap(
        error=None,
        content=probgrid
    )