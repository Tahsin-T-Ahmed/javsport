from src.components import schedule_banner, table_list
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list,
    upload_handler: function,
):
    
    view_tabs = st.tabs(["Results", "Data"])

    with view_tabs[0]:
        if required_files_list:
            for required_file in required_files_list:
                upload_handler(
                    file_name=required_file["name"],
                    file_type=required_file["type"],
                    sport_key=sport_key,
                    sport_title=sport_title,
                    label_urls_dict=required_file["label_urls_dict"]
                )
        else:
            st.session_state[sport_key]["file_requirements"] = dict(
                fulfilled=True
            )

    with view_tabs[1]:
        schedule_banner.render(
            schedule_df=st.session_state[sport_key]["schedule"]["display"]
        )

        if "leaderboards" in st.session_state[sport_key]:
            table_list.render(
                title="LEADERBOARDS",
                dataframes_dict=st.session_state[sport_key]["leaderboards"],
                collapse=True,
                hide_index=True
            )