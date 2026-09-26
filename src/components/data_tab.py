from src.components import schedule_banner, table_list
import streamlit as st

def render(sport_key: str):
    schedule_banner.render(
        schedule_df=st.session_state[sport_key]["schedule"]["display"]
    )

    if "leaderboards" not in st.session_state[sport_key]:
        return
    
    table_list.render(
        title="LEADERBOARDS",
        dataframes_dict=st.session_state[sport_key]["leaderboards"],
        collapse=True,
        hide_index=True
    )

    if not st.session_state[sport_key]["file_requirements"]["fulfilled"]:
        return

    table_list.render(
        title="UPLOADED FILES",
        dataframes_dict=st.session_state[sport_key]["file_requirements"]["data"]
    )