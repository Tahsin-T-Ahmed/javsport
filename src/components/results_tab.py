from src.components import upload_dialog
from src.data_collection.data_maps import RequiredFileMap
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[RequiredFileMap]
):
    if not st.session_state[sport_key]["file_requirements"]["fulfilled"]:
        st.subheader("Files required:")

        for file in required_files_list:
            color = None
            icon = None

            if st.session_state[sport_key]["file_requirements"]["data"][file["file_key"]] is not None:
                color = "green"
                icon = ":material/check:"
            else:
                color = "orange"
                icon = ":material/upload:"
            st.write(f"- :{color}[{sport_title} {file['file_label']} {icon}]")

        return

    st.write("File requirements met")