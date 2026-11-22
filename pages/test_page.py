import streamlit as st

from src.data_collection.parsers.scan_nba_team_xpm import scan_nba_team_xpm

file = st.file_uploader(
    label="Upload NBA Team-XPM File",
    type="csv"
)

if file:
    xpm_map = scan_nba_team_xpm(file)

    if xpm_map["error"]:
        st.error(xpm_map["error"])
    else:
        xpm = xpm_map["content"]
        st.write(xpm)