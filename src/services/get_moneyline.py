import datetime
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.parsers import scan_odds_table
from streamlit.typing import UploadedFile

def get_moneyline(
    uploaded_file: UploadedFile,
    timestamp: datetime.datetime
) -> DataFrameMap:
    pass