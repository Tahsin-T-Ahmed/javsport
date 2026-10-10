import streamlit as st

from src.services.get_team_roster import get_team_roster

get_team_roster(
    url="https://www.teamrankings.com/mlb/teams/"
)["content"]