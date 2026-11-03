import streamlit as st

import pandas as pd
from src.data_collection.scrapers.scan_match_results import scan_match_results
from src.services.get_outcomes import get_outcomes

match_url = st.text_input("Enter Match URL:")
if st.button("Confirm URL"):
    scoreboard_map = scan_match_results(match_url)

    if scoreboard_map["error"]:
        st.error(scoreboard_map["error"])
    else:
        scoreboard = scoreboard_map["content"]
        st.write(scoreboard)
    

file = st.file_uploader("Upload Wagers File")

if file:
    st.write(pd.read_csv(file))
    if st.button(":material/upload: Submit"):
        with st.spinner("Loading outcomes..."):
            outcomes_map = get_outcomes(
                file=file,
                winner_picks_url="https://www.teamrankings.com/nfl-win-picks/",
                # winner_picks_url=None,
            )

            if outcomes_map["error"]:
                st.error(outcomes_map["error"])
            else:

                outcomes = outcomes_map["content"]
                st.write(outcomes)