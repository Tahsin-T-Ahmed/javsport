from src.components import schedule_banner, table, table_list
import streamlit as st

def render(
    sport_key: str,
    sport_title: str
):
    schedule_banner.render(
        schedule_df=st.session_state[sport_key]["schedule"]["display"],
        sport_title=sport_title
    )

    if st.session_state[sport_key]["file_requirements"]["fulfilled"]:
        table_list.render(
            title=f"Uploaded {sport_title} Data",
            dataframes_dict=st.session_state[sport_key]["file_requirements"]["data"],
            collapse=True,
            hide_index=True,
            height="auto"
        )

    if ("team_roster" in st.session_state[sport_key]):
        table.render(
            label=f"{sport_title} Team-Roster",
            data=st.session_state[sport_key]["team_roster"],
            hide_index=True,
            collapse=True,
            height=300
        )

    if (
        "leaderboards" in st.session_state[sport_key]
        and
        st.session_state[sport_key]["leaderboards"]
    ):    
        table_list.render(
            title=f"{sport_title} Leaderboards",
            dataframes_dict=st.session_state[sport_key]["leaderboards"],
            collapse=True,
            hide_index=True,
            height=300
        )