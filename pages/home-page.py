from datetime import datetime
import streamlit as st

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
    body = "Choose a **SPORT** from the top menu (press the :material/double_arrow: arrow icon if using a mobile device), or from the shortcuts below:",
    text_alignment = "center"
)

with st.container(horizontal = True, horizontal_alignment = "center"):
    st.page_link("./pages/mlb-page.py", label="MLB :material/sports_baseball:")
    st.page_link("./pages/nba-page.py", label="NBA :material/sports_basketball:")
    st.page_link("./pages/ncaab-page.py", label="NCAAB :material/sports_basketball:")
    st.page_link("./pages/ncaaf-page.py", label="NCAAF :material/sports_football:")
    st.page_link("./pages/nfl-page.py", label="NFL :material/sports_football:")
    st.page_link("./pages/wnba-page.py", label="WNBA :material/sports_basketball:")

st.markdown(
    body = "JavSport calculates wager probabiltiies for upcoming games on the :green[current day] and :orange[minute]",
    text_alignment = "center"
)

now = datetime.now()

st.markdown(
    body = f"##### Time Now: :green[{now.strftime('%Y, %B %d')}] | :orange[{now.strftime('%I:%m %p')}]",
    text_alignment = "center"
)

st.markdown(
    body = "### :red[**WARNING:**] DATA IS TIME-SENSITIVE",
    text_alignment = "center"
)

st.markdown(
    body = "All calculations use the data available during the moment each webpage is loaded.",
    text_alignment = "center"
)