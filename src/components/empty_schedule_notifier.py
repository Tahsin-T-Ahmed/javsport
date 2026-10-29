import datetime
import streamlit as st
from src.utils.get_formatted_date import get_formatted_date

def render(
    sport_name: str,
    timestamp: datetime.datetime
):    
    date_f = get_formatted_date(timestamp)
    
    st.info(
        f"No {sport_name} games scheduled for {date_f}"
	)