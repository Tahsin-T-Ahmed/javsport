import datetime
from src.components import delay_disclaimer, page_header_banner, sport_page_body
from src.data_collection.data_maps import RequiredFileMap
from src.services.get_schedule import get_schedule
from src.services.load_schedule import load_schedule
import streamlit as st

def render(
    sport_name: str,
    sport_subheader: str,
    sport_icon: str,
    schedule_url: str,
    leaderboard_urls_dict: dict,
    metrics_assembler: callable,
    timestamp: datetime.datetime,
    win_trends_url: str | None = None,
    required_files_list: list[RequiredFileMap] | None = None,
):
    sport_title, sport_key = sport_name.upper(), sport_name.lower()

    st.set_page_config(
        page_title=f"JavSport - Wager {sport_title}",
        layout="centered"
    )

    session_state_preview = st.empty()

    page_header_banner.render(
        title=sport_title,
        subheader=sport_subheader,
        icon=sport_icon
    )

    sport_page_body.render(
        sport_key=sport_key,
        sport_title=sport_title,
        schedule_url=schedule_url,
        timestamp=timestamp,
        required_files_list=required_files_list,
        leaderboard_urls_dict=leaderboard_urls_dict,
        win_trends_url=win_trends_url,
        metrics_assembler=metrics_assembler
    )

    if sport_key in st.session_state and "schedule" in st.session_state[sport_key]:

        st.button(
            type="primary",
            label=f":material/refresh: Reload {sport_title} Data :material/refresh:",
            width="stretch",
            on_click=load_schedule,
            args=[sport_key, sport_title, timestamp, schedule_url, required_files_list]
        )

    delay_disclaimer.render()

    # session_state_preview.write(st.session_state)