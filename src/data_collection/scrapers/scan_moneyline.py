from bs4 import BeautifulSoup
import datetime
import pandas as pd
import streamlit as st
from streamlit.typing import UploadedFile
from src.data_collection.data_maps import DataFrameMap
from src.utils.get_date_ordinal_suffix import get_date_ordinal_suffix

def scan_moneyline(
    file: UploadedFile,
    timestamp: datetime.datetime
) -> DataFrameMap:
    year = timestamp.year
    month = timestamp.strftime('%B')
    day = timestamp.day
    weekday = timestamp.strftime("%A")
    day_ordinal_suffix = get_date_ordinal_suffix(day)
    date_str = f"{weekday}, {month} {day}{day_ordinal_suffix}, {year}"
    
    soup = BeautifulSoup(file)

    modules = soup.select("div[class*=module]:not([class*=ajax]):not([class*=-in])")

    for module in modules:
        date_header = module.find("h2").text
        st.write(f"Date header: {date_header}")
        st.write(f"Date string: {date_str}")
        st.write(f"Equal? {date_header == date_str}")