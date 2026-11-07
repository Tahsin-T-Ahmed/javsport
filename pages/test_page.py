import streamlit as st

import pandas as pd
from src.services.get_outcomes import get_outcomes
from src.services.get_team_roster import get_team_roster
from src.services.get_win_trends import get_win_trends

win_trends = None
wintrends_map = get_win_trends("https://www.teamrankings.com/nfl/trends/win_trends/")
if wintrends_map["error"]:
    st.error(wintrends_map["error"])
else:
    win_trends = wintrends_map["content"]

file = st.file_uploader(
    label="Upload Wagers File",
    type="csv"
)

team_roster = None
team_roster_map = get_team_roster("https://www.teamrankings.com/nfl/teams/")
if team_roster_map["error"]:
    st.error(team_roster_map["error"])
else:
    team_roster = team_roster_map["content"]

if (
    win_trends is not None and
    team_roster is not None and
    file
):
    outcomes_container = st.empty()

    loading_container = st.empty()
    with loading_container.container():
        progress_bar = st.progress(
            value=0.0
        )

        outcomes_map = get_outcomes(
            file=file,
            winner_picks_url="https://www.teamrankings.com/nfl-win-picks/",
            win_trends_df=win_trends,
            team_roster_df=team_roster,
            progress_bar=progress_bar
            # winner_picks_url=None,
        )

        if outcomes_map["error"]:
            outcomes_container.error(outcomes_map["error"])
        else:
            outcomes = outcomes_map["content"]
            outcomes_container.write(outcomes)

            # loading_container.empty()