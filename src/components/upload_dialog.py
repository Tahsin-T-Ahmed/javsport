import streamlit as st

def render(
    file_name: str,
    file_type: str,
    sport_key: str,
    sport_title: str,
    label_urls_dict: dict | None = None
):
    with st.container(border=True):
        file = st.file_uploader(
            label=f"Upload {sport_title} {file_name}:",
            type=file_type
        )

        for page_key, page_url in label_urls_dict.items():
            st.write(f"[{sport_title} {page_key}]({page_url})")

        if not file:
            return
        
        st.write(file)