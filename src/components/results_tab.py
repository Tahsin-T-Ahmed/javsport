import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list,
    upload_handler: function
):
    if required_files_list:
        for required_file in required_files_list:
            upload_handler(
                file_name=required_file["name"],
                file_type=required_file["type"],
                sport_key=sport_key,
                sport_title=sport_title,
                label_urls_dict=required_file["label_urls_dict"]
            )

        return
    
    st.session_state[sport_key]["file_requirements"] = dict(
        fulfilled=True
    )