from src.components import header, table
from src.services.get_outcomes import get_outcomes
import streamlit as st

def render(
    sport_title: str,
    winner_picks_url: str | None
):
    header.render(f"{sport_title} OUTCOMES")

    file = None

    with st.container(border=True):
        file = st.file_uploader(
            label=f"Upload :orange[{sport_title}] Wagers :green[Spreadsheet :material/view_list:]",
            type="csv"
        )

    if not file:
        return

    loading_container = st.empty()

    outcomes = None

    with loading_container.container():
        with st.spinner("Loading Outcomes..."):
            progress_bar = st.progress(
                value=0.0
            )

            outcomes_map = get_outcomes(
                file=file,
                winner_picks_url=winner_picks_url,
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
        label=f"{sport_title} Outcomes",
        hide_index=True
    )