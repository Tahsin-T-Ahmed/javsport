from src.components import schedule_banner, table_list
import streamlit as st

def render(
    sport_key: str,
    sport_title: str
):
    schedule_banner.render(
        schedule_df=st.session_state[sport_key]["schedule"]["display"],
        sport_title=sport_title
    )

    if "leaderboards" not in st.session_state[sport_key]:
        return

    if not st.session_state[sport_key]["leaderboards"]:
        return
    
    table_list.render(
        title=f"{sport_title} Leaderboards",
        dataframes_dict=st.session_state[sport_key]["leaderboards"],
        collapse=True,
        hide_index=True
    )

    if not st.session_state[sport_key]["file_requirements"]["fulfilled"]:
        return

    table_list.render(
        title=f"Uploaded {sport_title} Data",
        dataframes_dict=st.session_state[sport_key]["file_requirements"]["data"],
        collapse=True,
        hide_index=True
    )