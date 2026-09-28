import streamlit as st
from src.components import (
    empty_schedule_notifier,
    file_upload_section,
    timestamp_banner,
    wager_tabs
)
from src.data_collection.data_maps import RequiredFileMap
from src.services.get_leaderboards import get_leaderboards

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[RequiredFileMap],
    leaderboard_urls_dict: dict,
    win_trends_url: str
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

    leaderboards_map = get_leaderboards(
        leaderboard_urls_dict=leaderboard_urls_dict,
        timestamp=st.session_state[sport_key]["timestamp"],
        win_trends_url=win_trends_url
    )

    if leaderboards_map["error"]:
        st.error(leaderboards_map["error"])
        return

    st.session_state[sport_key]["leaderboards"] = leaderboards_map["content"]

    file_upload_section.render(
        sport_key=sport_key,
        sport_title=sport_title,
        required_files_list=required_files_list
    )

    wager_tabs.render(
        sport_key=sport_key,
        sport_title=sport_title,
        required_files_list=required_files_list
    )