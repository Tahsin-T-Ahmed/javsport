import pandas as pd
import streamlit as st

def predict_mlb_match(match: pd.Series):
    st.write(match)
    st.divider()