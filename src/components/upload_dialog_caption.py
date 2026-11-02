import streamlit as st

def render(guide_type: str):
    if guide_type:
        guide_desc = "Instructions: "
        
        match(guide_type):
            case "spreadsheet":
                guide_desc += ":orange[:material/content_copy: Copy/Paste] the :green[ENTIRE table :material/table:] (with :blue[links :material/link_2:]) into a :green[spreadsheet :material/view_list:]"
            case "webpage":
                guide_desc += ":orange[:material/download_2: Download & Save :material/save:] the full :green[webpage :material/web:]"
            case _:
                guide_desc = "Please consult JavSport admins on how to process this data"
        
        st.caption(guide_desc)