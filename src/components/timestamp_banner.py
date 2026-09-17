import streamlit as st

def render(timestamp_f):
    ordinal_suffix = None
    last_date_char = timestamp_f["date"][-1]

    match(last_date_char):
        case '1': 
            ordinal_suffix = "st"
        case '2':
            ordinal_suffix = "nd"
        case '3':
            ordinal_suffix = "rd"
        case _:
            ordinal_suffix = "th"

    with st.container(
        border = True
    ):
        st.markdown(
            body = f"##### Button clicked on (timestamp):",
            text_alignment = "center"
        )

        st.markdown(
            body = f"##### :green[:material/date_range: {timestamp_f['date']}{ordinal_suffix}] | :orange[:material/schedule: {timestamp_f['clocktime']}]",
            text_alignment = "center"
        )

        st.markdown(
            body = f":blue[:material/globe_clock: Time Zone: {timestamp_f['timezone']}]",
            text_alignment = "center"
        )