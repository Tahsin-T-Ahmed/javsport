from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import empty_schedule_notifier
from src.components import timestamp_banner
from src.data_collection.parsers.make_leaderboard import make_leaderboard
from src.data_collection.parsers.make_schedule import make_schedule

st.set_page_config(
    page_title = "JavSport - Wager NCAAB",
    layout = "wide"
)

st.header(
    body = "JavSport - NCAAB",
    text_alignment = "center"
)

st.markdown(
    body = "#### :material/sports_basketball: College Basketball :material/sports_basketball:",
    text_alignment = "center"
)

st.divider()

moneyline_col, load_button_col = st.columns(2)

def load_button_handler():
    st.session_state["ncaab"] = dict(
        timestamp = datetime.now()
    )

    schedule_map = make_schedule(
        schedule_url = "https://www.teamrankings.com/ncb/schedules/season/?week=0",
        timestamp = st.session_state["ncaab"]["timestamp"]
    )

    if schedule_map["error"]:
        error = schedule_map["error"]
        st.error(error)
        return

    schedule = schedule_map["content"]
    st.session_state["ncaab"]["schedule"] = schedule

    if schedule.empty:
        return

with moneyline_col:
    st.text_area(
        "Enter Moneyline Data:",
        key = "ncaab_moneyline_data"
    )
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with load_button_col:
    if "ncaab" not in st.session_state:
        st.markdown(
            body = "Click below to see today's predictions",
            text_alignment = "center"
        )

    load_button_label = ":material/touch_app: Load NCAAB Wagers :material/touch_app:"

    if "ncaab" in st.session_state:
        load_button_label = ":material/refresh: Reload NCAAB Wagers :material/refresh:"

    load_button = st.button(
        type = "primary",
        label = load_button_label,
        width = "stretch",
        on_click = load_button_handler
    )

if "ncaab" in st.session_state:
    with load_button_col:
        timestamp_banner.render(
            timestamp = st.session_state["ncaab"]["timestamp"]
        )

    if st.session_state["ncaab"]["schedule"].empty:
        empty_schedule_notifier.render(
            sport_name = "College Basketball",
            timestamp = st.session_state["ncaab"]["timestamp"]
        )
    else:
        for key, value in st.session_state["ncaab"].items():
            key
            value

    delay_disclaimer.render()
else:
    with load_button_col:
        delay_disclaimer.render()