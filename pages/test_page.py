import streamlit as st

import datetime
from src.data_collection.scrapers.scan_table_at_date import scan_table_at_date

url = "https://www.teamrankings.com/ncf/schedules/season/?week=0"
timestamp = datetime.datetime.now()

x = scan_table_at_date(
    url=url,
    timestamp=timestamp
)

st.write(x)