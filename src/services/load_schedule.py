import datetime
from src.services.get_schedule import get_schedule
import streamlit as st

def load_schedule(
    sport_key: str,
    sport_title: str,
    timestamp: datetime.datetime,
    schedule_url: str
):
    st.session_state[sport_key]["timestamp"] = timestamp

    with st.spinner(
        text=f"Checking {sport_title} Schedule...",
        show_time=True
    ):
        schedule_dict_map = get_schedule(
            schedule_url=schedule_url,
            timestamp=timestamp
        )

        if schedule_dict_map["error"]:
            st.error(
                body = schedule_dict_map["error"],
                icon=":material/error:"
            )

            st.toast(
                body=f":red[Failed to load {sport_title} schedule]",
                icon=":material/error:"
            )

            return

        st.session_state[sport_key]["schedule"] = schedule_dict_map["content"]

        st.session_state[sport_key]["leaderboards"] = dict()