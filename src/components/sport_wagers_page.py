import datetime
from src.components import (
    delay_disclaimer,
    footer,
    outcomes_section,
    page_header_banner,
    sport_page_body
)
from src.data_collection.data_maps import RequiredFileMap
from src.services.load_schedule import load_schedule
import streamlit as st

@st.fragment
def render(
    sport_name: str,
    sport_subheader: str,
    sport_icon: str,
    schedule_url: str,
    leaderboard_urls_dict: dict,
    metrics_assembler: callable,
    timestamp: datetime.datetime,
    team_roster_url: str,
    win_trends_url: str | None = None,
    required_files_list: list[RequiredFileMap] | None = None,
    winner_picks_url: str | None = None
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

    page_tabs = st.tabs(["Wagers", "Outcomes"])

    with page_tabs[0]:
        sport_page_body.render(
            sport_key=sport_key,
            sport_title=sport_title,
            schedule_url=schedule_url,
            timestamp=timestamp,
            required_files_list=required_files_list,
            leaderboard_urls_dict=leaderboard_urls_dict,
            team_roster_url=team_roster_url,
            win_trends_url=win_trends_url,
            metrics_assembler=metrics_assembler
        )

    with page_tabs[1]:
        outcomes_section.render(
            sport_key=sport_key,
            sport_title=sport_title,
            team_roster_url=team_roster_url,
            win_trends_url=win_trends_url,
            winner_picks_url=winner_picks_url
        )

    if sport_key in st.session_state and "schedule" in st.session_state[sport_key]:

        if st.button(
            label=f":material/refresh: Reset {sport_title} Data :material/refresh:",
            width="stretch",
        ):
            load_schedule(sport_key, sport_title, timestamp, schedule_url, required_files_list)
            
            st.rerun()

    delay_disclaimer.render()

    footer.render()

    # session_state_preview.write(st.session_state[sport_key]["file_requirements"])