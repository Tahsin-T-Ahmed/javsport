from datetime import datetime
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
    st.session_state["mlb_data"] = {
        "timestamp": datetime.now()
    }

with st.columns(3)[1]:
    load_button = st.button(
        label = st.session_state["mlb_load_button_text"],
        width = "stretch",
        on_click = load_button_handler
    )

if "mlb_data" in st.session_state:
    timestamp = st.session_state["mlb_data"]["timestamp"]
    date_f = timestamp.strftime('%Y, %B %d')
    clocktime_f = timestamp.strftime('%I:%M:%S %p')
    timezone_f = timestamp.astimezone().tzname()

    with st.columns([1,2,1])[1]:
        with st.container(
            border = True
        ):

            st.markdown(
                body = f"##### Button clicked on (timestamp):",
                text_alignment = "center"
            )

            st.markdown(
                body = f"##### :green[{date_f}] | :orange[{clocktime_f}]",
                text_alignment = "center"
            )

            st.markdown(
                body = f"Time Zone: {timezone_f}",
                text_alignment = "center"
            )

        st.markdown(
            body = "This data is not real-time and may take a few seconds to load.",
            text_alignment = "center"
        )

        st.markdown(
            body = "Wager with caution, especially when live-betting.",
            text_alignment = "center"
        )