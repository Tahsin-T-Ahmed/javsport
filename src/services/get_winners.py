import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.services.get_winner_picks import get_winner_picks
from streamlit.typing import UploadedFile

def get_winners(
    file: UploadedFile,
    winner_picks_url: str | None
) -> DataFrameMap:
    pass