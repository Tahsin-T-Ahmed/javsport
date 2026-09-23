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
            label=f"Upload [{sport_title} {file_name} Data]({source_url}) as .{file_type} file",
            type=file_type
        )

        if not file:
            return
        
        st.write(file)