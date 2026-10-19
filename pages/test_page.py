import streamlit as st

import datetime
from src.data_collection.scrapers.scan_cfb_table import scan_cfb_table

fdpg = scan_cfb_table("https://cfbstats.com/2026/leader/national/team/offense/split01/category13/sort01.html")["content"]

st.write(fdpg)