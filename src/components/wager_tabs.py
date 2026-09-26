from src.components import data_tab, results_tab, upload_dialog
from src.data_collection.data_maps import RequiredFileMap
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[RequiredFileMap]
):

    for file_map in required_files_list:
        upload_dialog.render(
            **file_map,
            sport_key=sport_key,
            sport_title=sport_title,
            timestamp=st.session_state[sport_key]["timestamp"]
        )

    if all(
        st.session_state[sport_key]["file_requirements"]["data"][file] is not None
        for file in st.session_state[sport_key]["file_requirements"]["data"]
    ):
        st.session_state[sport_key]["file_requirements"]["fulfilled"] = True
    else:
        st.session_state[sport_key]["file_requirements"]["fulfilled"] = False
    
    view_tabs = st.tabs(["Results", "Data"])

    with view_tabs[0]:
        results_tab.render(
            sport_key=sport_key,
            sport_title=sport_title,
            required_files_list=required_files_list
        )

    with view_tabs[1]:
        data_tab.render(sport_key=sport_key)