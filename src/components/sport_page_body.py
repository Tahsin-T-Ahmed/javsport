import datetime
import streamlit as st
from src.components import (
    empty_schedule_notifier,
    file_upload_section,
    timestamp_banner,
    wager_tabs
)
from src.data_collection.data_maps import RequiredFileMap
from src.services.get_leaderboards import get_leaderboards
from src.services.load_schedule import load_schedule

def render(
    sport_key: str,
    sport_title: str,
    schedule_url: str,
    timestamp: datetime.datetime,
    required_files_list: list[RequiredFileMap],
    leaderboard_urls_dict: dict,
    win_trends_url: str,
    metrics_assembler: callable
):
    if sport_key not in st.session_state:
        st.session_state[sport_key] = dict(
            file_requirements=dict(
                fulfilled=False,
                data={
                    file_map["file_key"]: None
                    for file_map in required_files_list
                }
            )
        )
    
    if "schedule" not in st.session_state[sport_key]:
        load_schedule(
            sport_key=sport_key,
            sport_title=sport_title,
            timestamp=timestamp,
            schedule_url=schedule_url
        )
    
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

    file_upload_section.render(
        sport_key=sport_key,
        sport_title=sport_title,
        required_files_list=required_files_list
        )

    if st.session_state[sport_key]["file_requirements"]["fulfilled"]:
        if not st.session_state[sport_key]["leaderboards"]:
            with st.spinner(
                text=f"Loading {sport_title} Leaderboards...",
                show_time=True
            ):
                progress_bar = st.progress(0.0)
                leaderboards_map = get_leaderboards(
                    leaderboard_urls_dict=leaderboard_urls_dict,
                    timestamp=st.session_state[sport_key]["timestamp"],
                    win_trends_url=win_trends_url,
                    progress_bar=progress_bar,
                    sport_title=sport_title
                )

                if leaderboards_map["error"]:
                    st.error(leaderboards_map["error"])
                    return

                st.session_state[sport_key]["leaderboards"] = leaderboards_map["content"]
                
                progress_bar.empty()

    wager_tabs.render(
        sport_key=sport_key,
        sport_title=sport_title,
        required_files_list=required_files_list,
        metrics_assembler=metrics_assembler
    )