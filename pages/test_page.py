import streamlit as st

from src.data_collection.builders.make_winner_picks import make_winner_picks

file = st.file_uploader("Upload Wagers File")

if file:

    winner_picks_map = make_winner_picks(
        url="https://www.teamrankings.com/nfl-win-picks/"
    )

    if winner_picks_map["error"]:
        st.error(winner_picks_map["error"])
    else:

        winner_picks = winner_picks_map["content"]
        st.write(winner_picks)