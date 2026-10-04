import streamlit as st

from bs4 import BeautifulSoup
import datetime
from src.data_collection.parsers.scan_odds_table import scan_odds_table

file = st.file_uploader(
    label="Upload Moneyline",
    type="mhtml"
)

if file is not None:
    timestamp = datetime.datetime.now()
    soup = scan_odds_table(
        file=file,
        timestamp=timestamp
    )

    st.write(soup)