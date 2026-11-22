import streamlit as st

from src.data_collection.builders.make_nba_team_xpm import make_nba_team_xpm

file = st.file_uploader(
    label="Upload NBA Team-XPM File",
    type="csv"
)

if file:
    xpm_map = make_nba_team_xpm(file)

    if xpm_map["error"]:
        st.error(xpm_map["error"])
    else:
        xpm = xpm_map["content"]
        st.write(xpm)