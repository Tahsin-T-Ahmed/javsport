import datetime
import streamlit as st

def render(
    file_label: str,
    file_key: str,
    file_type: str,
    sport_key: str,
    sport_title: str,
    file_parser: function,
    timestamp: datetime.datetime,
    guide_desc: str | None = None,
    source_url: str | None = None
):    
    st.session_state[sport_key]["file_requirements"]["data"][file_key] = None
    
    with st.container(border=True):
        label = f"Upload {sport_title} {file_label} Data"

        if source_url:
            label = f"Upload [{sport_title} {file_label} Data]({source_url})"

        label += f" as :orange[.{file_type} file]"

        file = st.file_uploader(
            label=label,
            type=file_type
        )

        if guide_desc:
            st.write(guide_desc)

        if not file:
            return

        table_map = file_parser(
            file=file,
            timestamp=timestamp
        )
        if table_map["error"]:
            st.error(table_map["error"])
            return

        table = table_map["content"]

        if table.empty:
            st.warning(
                title="DATA NOT DETECTED",
                body=f"No valid data could be extracted from the file: :red[{file.name}]",
                icon=":material/warning:"
            )
            st.markdown("Make sure:")
            st.markdown("""
            - the file contains data for the :green[current date]
            - it has the correct :orange[file type (extension)]
            - the data is properly formatted
            """)
            st.write("Then, try again")
            return

        st.session_state[sport_key]["file_requirements"]["data"][file_key] = table

        st.success(
            title="SCAN SUCCESSFUL!",
            body="Re-upload new file to overwrite",
            icon=":material/check:"
        )

        st.dataframe(
            data=table,
            height=200,
            hide_index=True
        )
        
        st.caption(f"Data extracted from :green[{file.name}]")