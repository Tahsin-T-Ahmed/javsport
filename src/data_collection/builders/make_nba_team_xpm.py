import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers.scan_nba_team_xpm import scan_nba_team_xpm
from streamlit.typing import UploadedFile

def make_nba_team_xpm(
    file: UploadedFile
) -> DataFrameMap:
    xpm_map = scan_nba_team_xpm(file)
    bbi_glossary = pd.read_csv("./src/glossaries/nba/teams_basketballindex.csv")

    if xpm_map["error"]:
        return DataFrameMap(
            error=xpm_map["error"],
            content=None
        )

    xpm_df = xpm_map["content"]

    xpm_df = xpm_df[[1, 3, 4, 5]]

    column_names = ["TEAM BBI NAME", "XPM OFFENSE", "XPM DEFENSE", "XPM NET"]

    xpm_df.columns = column_names

    xpm_df["TEAM TR NAME"] = xpm_df["TEAM BBI NAME"].apply(
        lambda bbi_name: bbi_glossary.loc[
            bbi_name.strip() == bbi_glossary["BASKETBALLINDEX"].str.strip(),
            "TEAMRANKINGS"
        ].item().strip()
    )

    return DataFrameMap(
        error=None,
        content=xpm_df
    )