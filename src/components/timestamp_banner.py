from datetime import datetime
from src.utils.format_timestamp import format_timestamp
import streamlit as st

def render(timestamp: datetime.datetime):
    timestamp_f = format_timestamp(timestamp)
    
    with st.container(
        border = True
    ):
        st.markdown(
            body = f"##### Button clicked on (timestamp):",
            text_alignment = "center"
        )

        st.markdown(
            body = f"##### :green[:material/date_range: {timestamp_f['date']}] | :orange[:material/schedule: {timestamp_f['clocktime']}]",
            text_alignment = "center"
        )

        st.markdown(
            body = f":blue[:material/globe_clock: Time Zone: {timestamp_f['timezone']}]",
            text_alignment = "center"
        )