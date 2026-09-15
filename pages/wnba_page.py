from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import timestamp_banner
from src.utils import format_timestamp

st.set_page_config(
    page_title = "JavSport - WNBA Calculator",
    layout = "wide"
)

st.header(
    body = "JavSport - WNBA",
    text_alignment = "center"
)

moneyline_col, load_button_col = st.columns(2)

if "wnba_load_button_text" not in st.session_state:
    st.session_state["wnba_load_button_text"] = "Load WNBA Wagers"

def load_button_handler():
    st.session_state["wnba_load_button_text"] = "Refresh WNBA Wagers"
    st.session_state["wnba_data"] = {
        "timestamp": datetime.now()
    }

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
    load_button = st.button(
        type = "primary",
        label = st.session_state["wnba_load_button_text"],
        width = "stretch",
        on_click = load_button_handler
    )

if "wnba_data" in st.session_state:
    timestamp_f = format_timestamp.format(st.session_state["wnba_data"]["timestamp"])

    with load_button_col:
        timestamp_banner.render(timestamp_f)

    delay_disclaimer.render()
else:
    with load_button_col:
        delay_disclaimer.render()
