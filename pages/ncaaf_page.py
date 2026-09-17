from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import empty_schedule_notifier
from src.components import timestamp_banner
from src.data_collection.parsers.make_leaderboard import make_leaderboard
from src.data_collection.parsers.make_schedule import make_schedule

st.set_page_config(
    page_title = "JavSport - Wager NCAAF",
    layout = "wide"
)

st.header(
    body = "JavSport - NCAAF",
    text_alignment = "center"
)

st.markdown(
    body = "#### :material/sports_football: College Football :material/sports_football:",
    text_alignment = "center"
)

st.divider()

moneyline_col, load_button_col = st.columns(2)

def load_button_handler():    
    st.session_state["ncaaf"] = dict(
        timestamp = datetime.now()
    )

    schedule_soup = make_schedule(
        schedule_url = "https://www.teamrankings.com/ncf/schedules/season/?week=0",
        timestamp = st.session_state["ncaaf"]["timestamp"]
    )

    if schedule_soup["error"]:
        error = schedule_soup["error"]
        st.error(error)
        return

    schedule = schedule_soup["content"]
    st.session_state["ncaaf"]["schedule"] = schedule

    if schedule.empty:
        return

with moneyline_col:
    st.text_area("Enter Moneyline Data:")
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with load_button_col:
    if "ncaaf" not in st.session_state:
        st.markdown(
            body = "Click below to see today's predictions",
            text_alignment = "center"
        )

    load_button_label = ":material/touch_app: Load NCAAF Wagers :material/touch_app:"

    if "ncaaf" in st.session_state:
        load_button_label = ":material/refresh: Reload NCAAF Wagers :material/refresh:"
        
    load_button = st.button(
        type = "primary",
        label = load_button_label,
        width = "stretch",
        on_click = load_button_handler
    )

if "ncaaf" in st.session_state:
    with load_button_col:
        timestamp_banner.render(
            timestamp = st.session_state["ncaaf"]["timestamp"]
        )

    delay_disclaimer.render()

    if st.session_state["ncaaf"]["schedule"].empty:
        empty_schedule_notifier.render(
            sport_name = "College Football",
            timestamp = st.session_state["ncaaf"]["timestamp"]
        )
        
    else:
        for key, value in st.session_state["ncaaf"].items():
            key
            value
else:
    with load_button_col:
        delay_disclaimer.render()