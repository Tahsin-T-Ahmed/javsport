import datetime
from src.components import table
import streamlit as st

def render(
    file_label: str,
    file_key: str,
    file_type: str | list[str],
    sport_key: str,
    sport_title: str,
    file_parser: function,
    timestamp: datetime.datetime,
    guide_type: str | None = None,
    source_url: str | None = None
):
    initial_file_success = None

    if (
        file_key in st.session_state[sport_key]["file_requirements"]["data"]
        and
        st.session_state[sport_key]["file_requirements"]["data"][file_key] is not None
    ):
        initial_file_success = True
    else:
        initial_file_success = False

    st.session_state[sport_key]["file_requirements"]["data"][file_key] = None
    
    with st.container(border=True):
        label = f"Upload {sport_title} {file_label} Data"

        if source_url:
            label = f"Upload [{sport_title} {file_label} Data :material/open_in_new:]({source_url})"

        file_type_label_color = "green"
        file_type_label = f":{file_type_label_color}[.{file_type}]"

        if isinstance(file_type, list):
            file_type_label = f":{file_type_label_color}[.{file_type[0]}]"

            if len(file_type) > 2:
                file_type_label += "".join([f', :{file_type_label_color}[.{ft}]' for ft in file_type[1:-1]])
                file_type_label += ','

            file_type_label += f" or :{file_type_label_color}[.{file_type[-1]}]"

        label += f" as {file_type_label} file"

        file = st.file_uploader(
            label=label,
            type=file_type
        )

        caption_container = st.empty()

        with caption_container:
            if guide_type:
                guide_desc = "Instructions: "
                
                match(guide_type):
                    case "webpage":
                        guide_desc += ":orange[:material/download_2: Download & Save :material/save:] the full :green[webpage :material/web:]"
                    case "spreadsheet":
                        guide_desc += ":orange[:material/content_copy: Copy/Paste] the :green[ENTIRE table :material/table:] (with :blue[links :material/link_2:]) into a :green[spreadsheet :material/view_list:]"
                    case _:
                        guide_desc = "Please consult JavSport admins on how to process this data"
                
                st.caption(guide_desc)

        if not file:
            return

        table_map = file_parser(
            file=file,
            timestamp=timestamp
        )
        if table_map["error"]:
            st.error(table_map["error"])
            return

        table_df = table_map["content"]

        if table_df.empty:
            st.warning(
                title="DATA NOT DETECTED",
                body=f"No valid data could be extracted from the file: :red[{file.name}]",
                icon=":material/warning:"
            )
            st.markdown("Make sure:")
            st.markdown("""
            - the file contains data for the :green[current date]
            - it has the correct :orange[file type (extension)]
            - it contains the :violet[target data (e.g. IP, SIERA)]
            """)
            st.write("Then, try again")
            return
        
        st.session_state[sport_key]["file_requirements"]["data"][file_key] = table_df

        if not initial_file_success:
            st.toast(
                body=f":orange[{sport_title}] :green[{file_label}] Uploaded",
                icon=":material/check:"
            )

        caption_container.empty()

        table.render(
            data=table_df,
            label=f"{file_label} Data",
            collapse=True,
            hide_index=True
        )
        
        st.caption(f"Data extracted from :green[{file.name}]")