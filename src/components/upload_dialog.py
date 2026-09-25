import datetime
import streamlit as st

def render(
    file_label: str,
    file_key: str,
    file_type: str,
    sport_key: str,
    sport_title: str,
    callback_handler: function,
    timestamp: datetime.datetime,
    guide_desc: str | None = None,
    source_url: str | None = None
):
    with st.container(border=True):
        label = f"Upload {sport_title} {file_label} Data"

        if source_url:
            label = f"Upload [{sport_title} {file_label} Data]({source_url})"

        label += f" as .{file_type} file"

        file = st.file_uploader(
            label=label,
            type=file_type
        )

        if guide_desc:
            st.write(guide_desc)

        if not file:
            return
        
        callback_handler(
            file=file,
            timestamp=timestamp
        )