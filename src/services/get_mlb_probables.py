import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers.scan_mlb_probables import scan_mlb_probables
from streamlit.delta_generator import DeltaGenerator
from streamlit.typing import UploadedFile

def get_mlb_probables(
    file: UploadedFile,
    progress_bar: DeltaGenerator | None = None,
    **kwargs
) -> DataFrameMap:
    team_glossary = pd.read_csv("./src/glossaries/mlb/teams_fangraphs.csv")
    
    probables_map = scan_mlb_probables(
        file=file,
        progress_bar=progress_bar,
        **kwargs
    )

    if probables_map["error"]:
        return DataFrameMap(
            error=probables_map["error"],
            content=None
        )

    probables = probables_map["content"]

    probables.drop(
        probables[("" == probables["FG TEAM"]) | (probables["FG TEAM"].isna())].index,
        inplace=True
    )

    probables["TR TEAM"] = probables["FG TEAM"].map(
        lambda fg_team: (
            team_glossary.loc[
                team_glossary["FANGRAPHS"] == fg_team,
                "TEAMRANKINGS"
            ].item().strip()
            if fg_team and any(team_glossary["FANGRAPHS"].str.contains(fg_team))
            else None
        )
    )

    return DataFrameMap(
        error=None,
        content=probables
    )