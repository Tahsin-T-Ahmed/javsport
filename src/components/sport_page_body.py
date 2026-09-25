import streamlit as st
from src.components import (
    empty_schedule_notifier,
    timestamp_banner,
    wager_tabs
)
from src.data_collection.data_maps import RequiredFileMap

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[RequiredFileMap]
):
    if sport_key not in st.session_state:
        st.session_state[sport_key] = dict()
    
    if "schedule" not in st.session_state[sport_key]:
        st.markdown(
            body="Click below to see today's predictions",
            text_alignment="center"
        )

        return
    
    timestamp_banner.render(
        timestamp=st.session_state[sport_key]["timestamp"],
        header="Loaded on (TIMESTAMP):"
    )

    if st.session_state[sport_key]["schedule"]["data"].empty:
        empty_schedule_notifier.render(
            sport_name=sport_title,
            timestamp=st.session_state[sport_key]["timestamp"]
        )

        return

    wager_tabs.render(
        sport_key=sport_key,
        sport_title=sport_title,
        required_files_list=required_files_list
    )