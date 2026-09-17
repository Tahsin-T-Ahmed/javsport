from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import timestamp_banner
from src.data_collection.get_leaderboard import get_leaderboard
from src.data_collection.get_schedule import get_schedule
from src.utils import format_timestamp

st.set_page_config(
    page_title = "JavSport - Wager NCAAF",
    layout = "wide"
)

st.header(
    body = "JavSport - NCAAF :material/sports_football:",
    text_alignment = "center"
)

st.markdown(
    body = "#### NCAA Football", 
    text_alignment = "center"
)

st.divider()

moneyline_col, load_button_col = st.columns(2)

if "ncaaf_load_button_text" not in st.session_state:
    st.session_state["ncaaf_load_button_text"] = ":material/touch_app: Load NCAAF Wagers :material/touch_app:"

def load_button_handler():
    st.session_state["ncaaf_load_button_text"] = ":material/refresh: Reload NCAAF Wagers :material/refresh:"

    now = datetime.now()
    
    st.session_state["ncaaf_data"] = {
        "timestamp": now
    }

    schedule_soup = get_schedule(
        schedule_url = "https://www.teamrankings.com/ncf/schedules/season/?week=0",
        timestamp = now
    )

    if schedule_soup["error"]:
        error = schedule_soup["error"]
        st.error(error)
        return

    schedule = schedule_soup["content"]
    st.session_state["ncaaf_data"]["schedule"] = schedule

with moneyline_col:
    st.text_area(
        "Enter Moneyline Data:",
        key = "ncaaf_moneyline_data"
    )
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with load_button_col:
    if "ncaaf_data" not in st.session_state:
        st.markdown(
            body = "Click below to see today's predictions",
            text_alignment = "center"
        )
    load_button = st.button(
        type = "primary",
        label = st.session_state["ncaaf_load_button_text"],
        width = "stretch",
        on_click = load_button_handler
    )

if "ncaaf_data" in st.session_state:
    timestamp_f = format_timestamp.format(st.session_state["ncaaf_data"]["timestamp"])

    with load_button_col:
        timestamp_banner.render(timestamp_f)

    delay_disclaimer.render()

    for key, value in st.session_state["ncaaf_data"].items():
        key
        value
else:
    with load_button_col:
        delay_disclaimer.render()