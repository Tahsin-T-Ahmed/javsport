import streamlit as st

st.set_page_config(
    page_title = "JavSport - MLB Calculator",
    layout = "wide"
)

st.header(
    body = "JavSport - MLB", 
    text_alignment = "center"
)

moneyline_col, siera_col = st.columns(2)

with moneyline_col:
    st.text_area(
        "Enter Moneyline Data:",
        key = "mlb_moneyline_data"
    )
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with siera_col:
    st.text_area(
        "Enter SIERA Data:",
        key = "mlb_siera_data"
    )
    
    st.button(
        label = "Parse SIERA Data",
        width = "stretch"
    )

if "mlb_load_button_text" not in st.session_state:
    st.session_state["mlb_load_button_text"] = "Load MLB Wagers"

def load_button_handler():
    st.session_state["mlb_load_button_text"] = "Refresh MLB Wagers"
    st.session_state["mlb_data"] = []

with st.columns(3)[1]:
    load_button = st.button(
        label = st.session_state["mlb_load_button_text"],
        width = "stretch",
        on_click = load_button_handler
    )

if "mlb_data" in st.session_state:
    "MLB Data Found"