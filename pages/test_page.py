import streamlit as st

from src.services.process_outcomes import process_outcomes

file = st.file_uploader("Upload Wagers File")

if file:

    outcomes = process_outcomes(
        file=file,
        winner_picks_url=None
    )["content"]

    st.write(outcomes)