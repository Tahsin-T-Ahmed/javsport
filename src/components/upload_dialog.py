import streamlit as st

def render(
    file_name: str,
    file_type: str,
    sport_key: str,
    sport_title: str,
    source_url: str | None = None
):
    with st.container(border=True):
        file = st.file_uploader(
            label=f"Upload {sport_title} {file_name}:",
            type=file_type
        )

        st.write(f"[{sport_title} {file_name}]({source_url})")

        if not file:
            return
        
        st.write(file)