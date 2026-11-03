import streamlit as st

import pandas as pd
from src.services.get_match_winner import get_match_winner
from src.services.get_outcomes import get_outcomes

match_url = st.text_input("Enter Match URL:")
if st.button("Confirm URL"):
    winner_map = get_match_winner(match_url)

    if winner_map["error"]:
        st.error(winner_map["error"])
    else:
        winner = winner_map["content"]
        st.write(winner)
    

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