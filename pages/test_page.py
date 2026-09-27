from bs4 import BeautifulSoup
import datetime
from src.data_collection.parsers.scan_mlb_starting_pitchers import scan_mlb_starting_pitchers
import streamlit as st

roster_file = st.file_uploader(
    label="Upload MLB Roster",
    type="xlsx"
)

if roster_file is not None:
    
    roster = scan_mlb_starting_pitchers(roster_file)
    st.write(roster["content"])