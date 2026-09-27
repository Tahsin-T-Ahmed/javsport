from bs4 import BeautifulSoup
import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from streamlit.typing import UploadedFile
from unidecode import unidecode

def scan_mlb_probables(file: UploadedFile, **kwargs) -> DataFrameMap:
    soup = BeautifulSoup(file)

    tbody = soup.find("tbody")
    if not tbody:
        return DataFrameMap(
            error="ERROR (MLB Probables-Scanner): Failed to scan TBODY of file",
            content=None
        )

    rows = tbody.find_all("tr")
    if not rows:
        return DataFrameMap(
            error=f"ERROR (MLB Probables-Scanner): Failed to scan ROWS of page",
            content=None
        )

    probgrid = pd.DataFrame()

    for row_idx, row in enumerate(rows):
        cells = row.find_all("td")
        if not cells:
            return DataFrameMap(
                error=f"ERROR (MLB Probables-Scanner): Failed to scan CELLS of row ({row})",
                content=None
            )

        if " " in cells[0].text:
            continue

        new_row_idx = probgrid.shape[0]

        pitcher_spans = cells[1].find_all("span")

        probgrid.loc[new_row_idx, "TEAM"] = cells[0].text
        probgrid.loc[new_row_idx, "N PITCHERS"] = len(pitcher_spans)

        for pitcher_idx, pitcher_span in enumerate(pitcher_spans):
            pitcher_name = pitcher_span.text.split("(")[0].strip()
            probgrid.loc[new_row_idx, f"PITCHER {pitcher_idx+1}"] = unidecode(pitcher_name)

            pitcher_links = pitcher_span.find_all("a")
            if not pitcher_links:
                continue

            if len(pitcher_links) > 1:
                return DataFrameMap(
                    error=f"ERROR (MLB Probables-Scanner): Multiple pitcher-links in ROW #{row_idx+1} for pitcher {pitcher_name}",
                    content=None
                )

            if not pitcher_links[0].has_attr("href"):
                continue

            pitcher_fgid = pitcher_links[0]["href"].split("/stats")[0].split("/")[-1]

            probgrid.loc[new_row_idx, f"PITCHER {pitcher_idx+1} FGID"] = pitcher_fgid

    return DataFrameMap(
        error=None,
        content=probgrid
    )