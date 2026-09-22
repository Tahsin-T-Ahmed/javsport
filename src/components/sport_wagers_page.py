import datetime
from src.components import (
    delay_disclaimer,
    page_header_banner,
    sport_page_body,
)
from src.services.get_leaderboards import get_leaderboards
from src.services.get_schedule import get_schedule
import streamlit as st

def handle_upload(
    file_name: str,
    file_type: str,
    sport_key: str,
    sport_title: str,
    label_urls_dict: dict | None = None
):
    with st.container(border=True):
        file = st.file_uploader(
            label=f"Upload {sport_title} {file_name}:",
            type=file_type
        )

        for page_key, page_url in label_urls_dict.items():
            st.write(f"[{sport_title} {page_key}]({page_url})")

        if file is not None:
            st.write(file)    

def load_button_handler(
    sport_key: str,
    timestamp: datetime.datetime | None,    # for testing purposes
    schedule_url: str,
    leaderboard_urls_dict: dict,
    win_trends_url: str | None = None
):
    if not timestamp:
        timestamp = datetime.datetime.now()
    
    st.session_state[sport_key]["timestamp"] = timestamp

    schedule_dict_map = get_schedule(
        schedule_url=schedule_url,
        timestamp=timestamp
    )

    if schedule_dict_map["error"]:
        st.error(schedule_dict_map["error"])
        return

    st.session_state[sport_key]["schedule"] = schedule_dict_map["content"]

    if st.session_state[sport_key]["schedule"]["data"].empty:
        return

    leaderboards_map = get_leaderboards(
        leaderboard_urls_dict=leaderboard_urls_dict,
        timestamp=timestamp,
        win_trends_url=win_trends_url
    )

    if leaderboards_map["error"]:
        st.error(leaderboards_map["error"])
        return

    st.session_state[sport_key]["leaderboards"] = leaderboards_map["content"]

def render(
    sport_name: str,
    sport_subheader: str,
    sport_icon: str,
    schedule_url: str,
    leaderboard_urls_dict: dict,
    win_trends_url: str | None = None,
    timestamp: datetime.datetime | None = None,
    required_files_list: list[dict] | None = None
):
    sport_title, sport_key = sport_name.upper(), sport_name.lower()

    st.set_page_config(
        page_title=f"JavSport - Wager {sport_title}",
        layout="centered"
    )

    page_header_banner.render(
        sport_title=sport_title,
        sport_subheader=sport_subheader,
        sport_icon=sport_icon
    )

    sport_page_body.render(
        sport_key=sport_key,
        sport_title=sport_title,
        required_files_list=required_files_list,
        upload_handler=handle_upload
    )

    load_button_label = f":material/touch_app: Load {sport_title} Wagers :material/touch_app:"

    if sport_key in st.session_state and "schedule" in st.session_state[sport_key]:
        load_button_label = f":material/refresh: Reload {sport_title} Wagers :material/refresh:"

    st.button(
        type="primary",
        label=load_button_label,
        width="stretch",
        on_click=load_button_handler,
        args=[sport_key, timestamp, schedule_url, leaderboard_urls_dict, win_trends_url]
    )

    delay_disclaimer.render()