import datetime
import streamlit as st

from src.data_collection.builders.make_tr_leaderboard import make_tr_leaderboard
from src.services.get_nba_team_xpm import get_nba_team_xpm

file = st.file_uploader(
    label="Upload NBA Team-XPM File",
    type="csv"
)

if file:
    xpm_map = get_nba_team_xpm(file)

    if xpm_map["error"]:
        st.error(xpm_map["error"])
    else:
        xpm = xpm_map["content"]
        st.write(xpm)

    leaderboard_map = make_tr_leaderboard(
        leaderboard_url="https://www.teamrankings.com/nba/stat/turnovers-per-game",
        timestamp=datetime.datetime.now()
    )

    if leaderboard_map["error"]:
        st.error(leaderboard_map["error"])
    else:
        leaderboard = leaderboard_map["content"]

        st.write(leaderboard)