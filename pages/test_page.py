import streamlit as st

import datetime
from src.services.get_ncaaf_dfei import get_ncaaf_dfei

dfei = get_ncaaf_dfei("https://bcftoys.com/2026-dfei")["content"]

st.write(dfei)