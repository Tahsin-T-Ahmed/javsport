from src.components import upload_dialog
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[dict]
):
    if required_files_list:
        for file_dict in required_files_list:
            upload_dialog.render(
                file_name=file_dict["file_name"],
                file_type=file_dict["file_type"],
                sport_key=sport_key,
                sport_title=sport_title,
                source_url=file_dict["source_url"]
            )

        return
    
    st.session_state[sport_key]["file_requirements"] = dict(
        fulfilled=True
    )