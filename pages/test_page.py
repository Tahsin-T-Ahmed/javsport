import streamlit as st

from src.data_collection.builders.make_wnba_team_lebron import make_wnba_team_lebron
from src.services.get_win_trends import get_win_trends

file = st.file_uploader(
    label="Upload WNBA Team-LEBRON",
    type="csv"
)

if file:
    wleb_map = make_wnba_team_lebron(file)

    if wleb_map["error"]:
        st.error(wleb_map["error"])
    else:
        wleb = wleb_map["content"]

        st.write(wleb)

        wintrends_map = get_win_trends(
            url="https://www.teamrankings.com/wnba/trends/win_trends/"
        )

        if wintrends_map["error"]:
            st.error(wintrends_map["error"])
        else:
            win_trends = wintrends_map["content"]

            st.write(win_trends)