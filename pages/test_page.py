import streamlit as st

import datetime
from src.data_collection.builders.make_ncaaf_dfei import make_ncaaf_dfei

dfei = make_ncaaf_dfei("https://bcftoys.com/2026-dfei")["content"]

st.write(dfei)