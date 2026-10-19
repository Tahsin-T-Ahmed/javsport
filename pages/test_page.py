import streamlit as st

import datetime
from src.data_collection.builders.make_cfb_statboard import make_cfb_statboard

fdpg = make_cfb_statboard("https://cfbstats.com/2026/leader/national/team/offense/split01/category13/sort01.html")["content"]

st.write(fdpg)