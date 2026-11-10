import streamlit as st

from src.services.get_outcomes import get_outcomes

file = st.file_uploader(
    label="Upload Wagers File",
    type="csv"
)

if file:
    outcomes_container = st.empty()

    loading_container = st.empty()
    with loading_container.container():
        progress_bar = st.progress(
            value=0.0
        )

        outcomes_map = get_outcomes(
            file=file,
            progress_bar=progress_bar
            # winner_picks_url=None,
        )

        if outcomes_map["error"]:
            outcomes_container.error(outcomes_map["error"])
        else:
            outcomes = outcomes_map["content"]
            outcomes_container.write(outcomes)

            # loading_container.empty()