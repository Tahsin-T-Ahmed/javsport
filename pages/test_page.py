import streamlit as st

import datetime
from src.data_collection.builders.make_win_trends import make_win_trends

make_win_trends(
    record_url="https://www.teamrankings.com/ncf/trends/win_trends/"
)["content"]