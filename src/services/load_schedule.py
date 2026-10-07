import datetime
from src.data_collection.data_maps import RequiredFileMap
from src.services.get_schedule import get_schedule
import streamlit as st

def load_schedule(
    sport_key: str,
    sport_title: str,
    timestamp: datetime.datetime,
    schedule_url: str,
    required_files_list: list[RequiredFileMap],
):
    st.session_state[sport_key]["timestamp"] = timestamp    
        
    st.session_state[sport_key]["file_requirements"]=dict(
        fulfilled=False,
        data={
            file_map["file_key"]: None
            for file_map in required_files_list
        }
    )

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