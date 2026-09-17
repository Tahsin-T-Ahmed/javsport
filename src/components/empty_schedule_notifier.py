from datetime import datetime
import streamlit as st
from src.utils.get_date_ordinal_suffix import get_date_ordinal_suffix

def render(sport_name: str, timestamp: datetime.datetime):
        year, month, day = timestamp.year, timestamp.strftime('%B'), timestamp.day
        day_ordinal_suffix = get_date_ordinal_suffix(day)
        
        st.info(f"No {sport_name} games scheduled for {month} {day}{day_ordinal_suffix}, {year}")