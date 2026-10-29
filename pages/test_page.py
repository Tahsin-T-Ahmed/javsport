import streamlit as st

import datetime
from src.data_collection.builders.make_tr_leaderboard import make_tr_leaderboard

lb = make_tr_leaderboard("https://www.teamrankings.com/nfl/stat/average-scoring-margin", datetime.datetime.now())["content"]

st.write(lb)