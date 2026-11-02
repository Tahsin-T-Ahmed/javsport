import streamlit as st

from src.services.process_outcomes import process_outcomes

cols = st.columns(2)

month = None
with cols[0]:
    month = st.number_input(
        label="Month",
        min_value=1,
        max_value=12
    )

day = None
with cols[1]:
    month = st.number_input(
        label="Day",
        min_value=1,
        max_value=31
    )


file = st.file_uploader("Upload Wagers File")

if file:
    if st.button(":material/upload: Submit"):
        outcomes = process_outcomes(
            file=file,
            winner_picks_url="https://www.teamrankings.com/nfl-win-picks/",
            month=month,
            day=day
        )

        if outcomes["error"]:
            st.error(outcomes["error"])
        else:

            outcomes = outcomes["content"]
            st.write(outcomes)