from src.components import page_header_banner, table
from src.services.get_outcomes import get_outcomes
import streamlit as st

def render():
    page_header_banner.render(
        title="Outcomes",
        subheader="Game Aftermaths",
        icon=":material/sports_score:"
    )
    
    file = None

    with st.container(border=True):
        file = st.file_uploader(
            label=f"Upload Wagers :green[Spreadsheet :material/view_list:]",
            type="csv"
        )

    if not file:
        return

    loading_container = st.empty()

    outcomes = None

    with loading_container.container():
        with st.spinner(
            text="Loading Outcomes...",
            show_time=True
        ):
            progress_bar = st.progress(
                value=0.0
            )

            outcomes_map = get_outcomes(
                file=file,
                progress_bar=progress_bar
            )

            if outcomes_map["error"]:
                st.error(outcomes_map["error"])
                return

            outcomes = outcomes_map["content"]

    if outcomes is None:
        return

    loading_container.empty()

    table.render(
        data=outcomes,
        label="Outcomes",
        height="auto",
        hide_index=True
    )