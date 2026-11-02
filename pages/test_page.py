import streamlit as st

import pandas as pd
from src.data_collection.scrapers.scan_tr_table import scan_tr_table

winner_picks = scan_tr_table(
    url="https://www.teamrankings.com/nfl-win-picks/"
)["content"]

st.write(winner_picks)