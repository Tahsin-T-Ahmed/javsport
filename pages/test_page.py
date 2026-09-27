from bs4 import BeautifulSoup
import datetime
from src.data_collection.parsers.scan_mlb_probables import scan_mlb_probables
import streamlit as st

pp = st.file_uploader("Upload Probables")

if pp is not None:
    
    probables = scan_mlb_probables(pp)
    st.write(probables)