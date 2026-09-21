from datetime import datetime
from src.utils.format_timestamp import format_timestamp
import streamlit as st

def render(
    timestamp: datetime.datetime,
    header: str = "TIMESTAMP:"
):
    timestamp_f = format_timestamp(timestamp)
    
    with st.container(
        border=True
    ):
        st.markdown(
            body=f"##### {header}",
            text_alignment="center",
            anchors=False
        )

        lcol, rcol = st.columns([1, 3, 2, 1])[1:3]

        with lcol:
            st.markdown(
                f"##### :green[:material/date_range: {timestamp_f['date']}]",
                text_alignment="center",
                anchors=False
            )

        with rcol:
            st.markdown(
                f"##### :orange[:material/schedule: {timestamp_f['clocktime']}]",
                text_alignment="center",
                anchors=False
            )

        st.markdown(
            body=f"###### :blue[:material/globe_clock: Time Zone: {timestamp_f['timezone']}]",
            text_alignment="center",
            anchors=False
        )