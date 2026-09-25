import datetime
from src.components import upload_dialog
from src.data_collection.scrapers.scan_odds_table import scan_odds_table
import streamlit as st

st.session_state

upload_dialog.render(
    file_label="Moneyline",
    file_key="moneyline",
    file_type="mhtml",
    sport_key="SPORTKEY",
    sport_title="SPORT-TITLE",
    file_parser=scan_odds_table,
    timestamp=datetime.datetime.now()
)