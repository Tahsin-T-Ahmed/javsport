import streamlit as st

import datetime
from src.data_collection.builders.make_cfb_leaderboard import make_cfb_leaderboard

fdpg = make_cfb_leaderboard("https://cfbstats.com/2026/leader/national/team/offense/split01/category13/sort01.html")["content"]

st.write(fdpg)