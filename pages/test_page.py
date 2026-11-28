import streamlit as st

from src.data_collection.parsers.scan_kenpom_table import scan_kenpom_table

file = st.file_uploader(
    label="Upload NCAAB Kenpom Data",
    type="csv"
)

if file:
    kenpom_map = scan_kenpom_table(file)
    if kenpom_map["error"]:
        st.error(kenpom_map["error"])
    else:
        kenpom = kenpom_map["content"]

        st.write(kenpom)