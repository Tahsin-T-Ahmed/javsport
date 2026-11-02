import streamlit as st

import datetime
from src.data_collection.builders.make_schedule import make_schedule

schedule = make_schedule(
    schedule_url="https://www.teamrankings.com/ncb/schedules/season/?week=0",
    timestamp=datetime.datetime.now()
)["content"]

st.write(schedule)