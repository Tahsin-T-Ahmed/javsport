from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import empty_schedule_notifier
from src.components import timestamp_banner
from src.data_collection.parsers.make_leaderboard import make_leaderboard
from src.data_collection.parsers.make_schedule import make_schedule

st.set_page_config(
    page_title = "JavSport - Wager WNBA",
    layout = "wide"
)

st.header(
    body = "JavSport - WNBA",
    text_alignment = "center"
)

st.markdown(
    body = "#### :material/sports_basketball: Women's NBA :material/sports_basketball:",
    text_alignment = "center"
)

st.divider()

moneyline_col, load_button_col = st.columns(2)

def load_button_handler():
    st.session_state["wnba"] = dict(
        timestamp = datetime.now()
    )

    schedule_map = make_schedule(
        schedule_url = "https://www.teamrankings.com/wnba/schedules/season/?week=0",
        timestamp = st.session_state["wnba"]["timestamp"]
    )

    if schedule_map["error"]:
        error = schedule_map["error"]
        st.error(error)
        return

    schedule = schedule_map["content"]
    st.session_state["wnba"]["schedule"] = schedule

    if schedule.empty:
        return

with moneyline_col:
    st.text_area(
        "Enter Moneyline Data:",
        key = "wnba_moneyline_data"
    )
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with load_button_col:
    if "wnba" not in st.session_state:
        st.markdown(
            body = "Click below to see today's predictions",
            text_alignment = "center"
        )

    load_button_label = ":material/touch_app: Load WNBA Wagers :material/touch_app:"

    if "wnba" in st.session_state:
        load_button_label = ":material/refresh: Reload WNBA Wagers :material/refresh:"
        
    load_button = st.button(
        type = "primary",
        label = load_button_label,
        width = "stretch",
        on_click = load_button_handler
    )

if "wnba" in st.session_state:
    with load_button_col:
        timestamp_banner.render(
            timestamp = st.session_state["wnba"]["timestamp"]
        )

    if st.session_state["wnba"]["schedule"].empty:
        empty_schedule_notifier.render(
            sport_name = "Women's NBA",
            timestamp = st.session_state["wnba"]["timestamp"]
        )

    else:
        for key, value in st.session_state["wnba"].items():
            key
            value

    delay_disclaimer.render()
else:
    with load_button_col:
        delay_disclaimer.render()
