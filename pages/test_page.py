import streamlit as st

import datetime
from src.data_collection.builders.make_cfbstats_leaderboard import make_cfbstats_leaderboard

fdpg = make_cfbstats_leaderboard("https://cfbstats.com/2026/leader/national/team/offense/split01/category13/sort01.html")["content"]

st.write(fdpg)