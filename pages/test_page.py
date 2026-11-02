import streamlit as st

from src.data_collection.builders.make_winner_picks import make_winner_picks

file = st.file_uploader("Upload Wagers File")

if file:

    winner_picks = make_winner_picks(
        url="https://www.teamrankings.com/nfl-win-picks/"
    )["content"]

    st.write(winner_picks)