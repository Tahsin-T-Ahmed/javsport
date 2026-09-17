from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import timestamp_banner
from src.data_collection.get_leaderboard import get_leaderboard
from src.data_collection.get_schedule import get_schedule
from src.utils import format_timestamp

st.set_page_config(
    page_title = "JavSport - NBA Calculator",
    layout = "wide"
)

st.header(
    body = "JavSport - NBA :material/sports_basketball:",
    text_alignment = "center"
)

moneyline_col, load_button_col = st.columns(2)

if "nba_load_button_text" not in st.session_state:
    st.session_state["nba_load_button_text"] = "Load NBA Wagers"

def load_button_handler():
    st.session_state["nba_load_button_text"] = "Refresh NBA Wagers"

    now = datetime.now()

    st.session_state["nba_data"] = {
        "timestamp": now
    }

    schedule_map = get_schedule(
        schedule_url = "https://www.teamrankings.com/nba/schedules/season/?week=0",
        timestamp = now
    )

    if schedule_map["error"]:
        error = schedule_map["error"]
        st.error(error)
        return

    schedule = schedule_map["content"]
    st.session_state["nba_data"]["schedule"] = schedule

with moneyline_col:
    st.text_area(
        "Enter Moneyline Data:",
        key = "nba_moneyline_data"
    )
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with load_button_col:
    load_button = st.button(
        type = "primary",
        label = st.session_state["nba_load_button_text"],
        width = "stretch",
        on_click = load_button_handler
    )

if "nba_data" in st.session_state:
    timestamp_f = format_timestamp.format(st.session_state["nba_data"]["timestamp"])

    with load_button_col:
        timestamp_banner.render(timestamp_f)

    for key, value in st.session_state["nba_data"].items():
        key
        value

    delay_disclaimer.render()
else:
    with load_button_col:
        delay_disclaimer.render()