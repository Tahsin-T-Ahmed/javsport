import streamlit as st

import pandas as pd
from src.services.get_outcomes import get_outcomes

cols = st.columns(2)


file = st.file_uploader("Upload Wagers File")

if file:
    st.write(pd.read_csv(file))
    if st.button(":material/upload: Submit"):
        with st.spinner("Loading outcomes..."):
            outcomes = get_outcomes(
                file=file,
                winner_picks_url="https://www.teamrankings.com/nfl-win-picks/",
                # winner_picks_url=None,
            )

        if outcomes["error"]:
            st.error(outcomes["error"])
        else:

            outcomes = outcomes["content"]
            st.write(outcomes)