from datetime import datetime
import streamlit as st
from src.utils import format_timestamp

st.set_page_config(
    page_title = "JavSport - Better Sports Better",
    layout = "centered"
)

st.title(
    body = "JavSport", 
    text_alignment = "center"
)

st.header(
    body = "Bet Smarter, Not Harder",
    text_alignment = "center"
)

st.divider()

st.markdown(
    body = "Choose a **SPORT** from the top menu (press :material/keyboard_double_arrow_right: on mobile), or from the shortcuts below:",
    text_alignment = "center"
)

with st.container(
    horizontal = True,
    horizontal_alignment = "center",
    border = True,
    gap = "medium"
):
    st.page_link("./pages/mlb_page.py", label="MLB :material/sports_baseball:")
    st.page_link("./pages/nba_page.py", label="NBA :material/sports_basketball:")
    st.page_link("./pages/ncaab_page.py", label="NCAAB :material/sports_basketball:")
    st.page_link("./pages/ncaaf_page.py", label="NCAAF :material/sports_football:")
    st.page_link("./pages/nfl_page.py", label="NFL :material/sports_football:")
    st.page_link("./pages/wnba_page.py", label="WNBA :material/sports_basketball:")

st.markdown(
    body = "JavSport calculates wager probabiltiies for upcoming games on the :green[current day] and :orange[time]",
    text_alignment = "center"
)

now = datetime.now()
timestamp_f = format_timestamp.format(now)

st.markdown(
    body = f"##### Time Now: :green[{timestamp_f['date']}] | :orange[{timestamp_f['clocktime']} ({timestamp_f['timezone']})]",
    text_alignment = "center"
)

st.space()

st.markdown(
    body = "### :red[**WARNING:**] DATA IS TIME-SENSITIVE",
    text_alignment = "center"
)

st.markdown(
    body = "All calculations use the data available during the moment each webpage is loaded.",
    text_alignment = "center"
)