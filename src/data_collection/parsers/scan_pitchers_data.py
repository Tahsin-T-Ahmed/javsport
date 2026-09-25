import datetime
import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from streamlit.typing import UploadedFile

import streamlit as st

def scan_pitchers_data(
    file: UploadedFile,
    timestamp: datetime.datetime
) -> DataFrameMap:
    st.write(file)