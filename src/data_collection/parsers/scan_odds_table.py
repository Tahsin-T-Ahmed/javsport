from bs4 import BeautifulSoup
import datetime
import pandas as pd
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile
from src.data_collection.data_maps import DataFrameMap
from src.utils.get_date_ordinal_suffix import get_date_ordinal_suffix

def scan_odds_table(
    file: UploadedFile,
    timestamp: datetime.datetime,
    progress_bar: DeltaGenerator | None = None
) -> DataFrameMap:
    year = timestamp.year
    month = timestamp.strftime('%B')
    day = timestamp.day
    weekday = timestamp.strftime("%A")
    day_ordinal_suffix = get_date_ordinal_suffix(day)
    date_str = f"{weekday}, {month} {day}{day_ordinal_suffix}, {year}"
    
    soup = BeautifulSoup(file)

    modules = soup.select("div[class*=module]:not([class*=ajax]):not([class*=-in])")
    if not modules:
        return DataFrameMap(
            error=f"ERROR (Odds-Scanner): No module-divs found in Odds page.",
            content=None
        )

    odds_df = pd.DataFrame()

    for module in modules:
        module_header = module.find("h2")
        if not module_header:
            continue

        module_date_raw = module_header.text

        module_date_clean = " ".join([
            date_term.strip() 
            for date_term in module_date_raw.split(" ")
            if "" != date_term
        ])

        if module_date_clean != date_str:
            continue

        subtables = module.find_all("table")
        if not subtables:
            continue

        n_subtables = len(subtables)
        
        for subtable_idx in range(n_subtables):
            subtable = subtables[subtable_idx]

            headers = subtable.find_all("th")
            if not headers:
                continue

            if progress_bar:
                progress_bar.progress(
                    value=subtable_idx/n_subtables,
                    text=f"Scanning match {subtable_idx+1} of {n_subtables} ({int(subtable_idx/n_subtables)}%)"
                )
            
            columns = [header.text.strip().upper() if ":" not in header.text else "TEAM" for header in headers]
            n_columns = len(columns)

            tbody = subtable.find("tbody")
            if not tbody:
                continue

            rows = tbody.find_all("tr")
            if not rows:
                continue

            subtable_df = pd.DataFrame()

            for row in rows:
                cells = row.find_all("td")
                if not cells:
                    continue

                if len(cells) < n_columns:
                    continue

                new_row_idx = subtable_df.shape[0]

                for cell, column in zip(cells, columns):
                    subtable_df.loc[new_row_idx, column] = cell.text

            subtable_df["TOTAL"] = subtable_df["TOTAL"].sum()

            odds_df = pd.concat(
                [odds_df, subtable_df],
                axis=0
            )

    odds_df.reset_index(drop=True, inplace=True)

    if "" in odds_df.columns:
        odds_df.drop(columns="", inplace=True)

    if progress_bar:
        progress_bar.status(
            label="Complete! :green[:material/check:]",
            state="complete"
        )

    return DataFrameMap(
        error=None,
        content=odds_df
    )