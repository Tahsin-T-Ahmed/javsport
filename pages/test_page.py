import datetime
from src.data_collection.builders.make_schedule import make_schedule
import streamlit as st

schedule_map = make_schedule(
    schedule_url="https://www.teamrankings.com/ncf/schedules/season/?week=0",
    timestamp=datetime.datetime.now()
)

schedule = None

if schedule_map["error"]:
    st.error(schedule_map)

else:
    schedule = schedule_map["content"]

    st.write(schedule)