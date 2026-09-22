import datetime
import streamlit as st
from src.utils.get_date_ordinal_suffix import get_date_ordinal_suffix

def render(sport_name: str, timestamp: datetime.datetime):
        year = timestamp.year
        month = timestamp.strftime('%B')
        day = timestamp.day
        weekday = timestamp.strftime("%A")
        day_ordinal_suffix = get_date_ordinal_suffix(day)
        
        st.info(f"No {sport_name} games scheduled for {weekday}, {month} {day}{day_ordinal_suffix}, {year}")