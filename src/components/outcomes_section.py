from src.components import header, table
from src.services.process_outcomes import process_outcomes
import streamlit as st

def render(
    sport_title: str,
    win_trends_url: str
):
    header.render(f"{sport_title} Outcomes")

    file = None

    with st.container(border=True):
        file = st.file_uploader(
            label=f"Upload :orange[{sport_title}] Wagers :green[Spreadsheet :material/view_list:]",
            type="csv"
        )

    if not file:
        return

    outcomes_map = process_outcomes(
        file=file,
        win_trends_url=win_trends_url
    )

    if outcomes_map["error"]:
        st.error(outcomes_map["error"])
        return

    outcomes = outcomes_map["content"]

    table.render(
        data=outcomes,
        label=f"{sport_title} Outcomes",
        hide_index=True
    )