from src.components import header, upload_dialog
from src.data_collection.data_maps import RequiredFileMap
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[RequiredFileMap]
):
    header.render("SUBMIT FILES FOR RESULTS")
    
    for req_file_idx, req_file_map in enumerate(required_files_list):
        if st.session_state[sport_key]["file_requirements"]["data"][req_file_map["file_key"]] is not None:
            continue
        
        upload_dialog.render(
            **req_file_map,
            sport_key=sport_key,
            sport_title=sport_title,
            timestamp=st.session_state[sport_key]["timestamp"]
        )

    if all(
        st.session_state[sport_key]["file_requirements"]["data"][file] is not None
        for file in st.session_state[sport_key]["file_requirements"]["data"]
    ):
        st.session_state[sport_key]["file_requirements"]["fulfilled"] = True