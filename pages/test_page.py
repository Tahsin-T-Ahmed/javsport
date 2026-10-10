import streamlit as st

from src.data_collection.builders.make_team_roster import make_team_roster

make_team_roster(
    url="https://www.teamrankings.com/mlb/teams/"
)["content"]