import streamlit as st

from src.services.get_outcomes import get_outcomes

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
    day = st.number_input(
        label="Day",
        min_value=1,
        max_value=31
    )


file = st.file_uploader("Upload Wagers File")

if file:
    if st.button(":material/upload: Submit"):
        outcomes = get_outcomes(
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