from src.components import header, predictions_section
from src.data_collection.data_maps import RequiredFileMap
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[RequiredFileMap],
    metrics_assembler: callable
):
    if not st.session_state[sport_key]["file_requirements"]["fulfilled"]:
        header.render(
            text="Files required:",
            text_alignment="left"
        )

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

    predictions_section.render(
        sport_key=sport_key,
        metrics_assembler=metrics_assembler
    )