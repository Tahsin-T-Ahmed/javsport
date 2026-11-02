import streamlit as st

from src.services.process_outcomes import process_outcomes

file = st.file_uploader("Upload Wagers File")

if file:

    outcomes = process_outcomes(
        file=file,
        winner_picks_url="https://www.teamrankings.com/nfl-win-picks/"
    )

    if outcomes["error"]:
        st.error(outcomes["error"])
    else:

        outcomes = outcomes["content"]
        st.write(outcomes)