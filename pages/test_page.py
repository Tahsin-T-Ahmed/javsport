import streamlit as st

import datetime
from src.data_collection.scrapers.scan_ncaaf_dfei import scan_ncaaf_dfei

dfei = scan_ncaaf_dfei("https://bcftoys.com/2026-dfei")["content"]

st.write(dfei)