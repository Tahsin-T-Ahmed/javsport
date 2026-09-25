from src.components import data_tab, results_tab
from src.data_collection.data_maps import RequiredFileMap
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[RequiredFileMap]
):
    
    view_tabs = st.tabs(["Results", "Data"])

    with view_tabs[0]:
        results_tab.render(
            sport_key=sport_key,
            sport_title=sport_title,
            required_files_list=required_files_list
        )

    with view_tabs[1]:
        data_tab.render(sport_key=sport_key)