from datetime import datetime
from src.components import footer
from src.utils.format_timestamp import format_timestamp
import streamlit as st

st.set_page_config(
    page_title="JavSport - Better Sports Better",
    layout="centered"
)

with st.container(border=True):
    st.title(
        body=":violet[JavSport]", 
        text_alignment="center",
        anchor=False
    )

    st.markdown(
        body="#### :rainbow[:material/money_bag: Bet Smarter, Not Harder :material/money_bag:]",
        text_alignment="center",
        anchors=False
    )

    st.space()

    st.markdown(
        body=":gray[:material/mic_off: Don't tell anyone about this website :material/mic_off:]",
        text_alignment="center",
        anchors=None
    )

st.markdown(
    body="Choose a **SPORT** from the top-left :material/north_west: menu or the shortcuts below :material/south::",
    text_alignment="center"
)

with st.container(
    horizontal=True,
    horizontal_alignment="center",
    border=True,
    gap="medium"
):
    st.page_link("./pages/mlb_page.py", label="MLB :material/sports_baseball:")
    st.page_link("./pages/nba_page.py", label="NBA :material/sports_basketball:")
    st.page_link("./pages/ncaab_page.py", label="NCAAB :material/sports_basketball:")
    st.page_link("./pages/ncaaf_page.py", label="NCAAF :material/sports_football:")
    st.page_link("./pages/nfl_page.py", label="NFL :material/sports_football:")
    st.page_link("./pages/wnba_page.py", label="WNBA :material/sports_basketball:")

st.markdown(
    body="JavSport calculates wagers for upcoming games on the :green[current day :material/date_range:] and :orange[time :material/schedule:]",
    text_alignment="center"
)

now = datetime.now()
timestamp_f = format_timestamp(now)

with st.container(horizontal=True, horizontal_alignment="center"):
    st.markdown(
        body=f"##### :green[:material/date_range: {timestamp_f['date']}]",
        anchors=False
    )

    st.markdown(
        body=f"##### :orange[:material/schedule: {timestamp_f['clocktime']}]",
        anchors=False
    )

    st.markdown(
        body=f"##### :blue[:material/globe_clock: {timestamp_f['timezone']}]",
        anchors=False
    )

with st.container(border=True):
    with st.container(
        horizontal=True,
        horizontal_alignment="center",
        gap="xsmall"
    ):
        st.markdown(
            body="### :red[:material/warning: WARNING:]",
            anchors=False
        )

        st.markdown(
            body="### DATA IS TIME-SENSITIVE",
            anchors=False
        )

    st.markdown(
        body=":material/timer_pause: Once the stats are loaded, they're STATIC :material/hourglass_pause:",
        text_alignment="center"
    )

    st.caption(
        body="No pun intended",
        text_alignment="center"
    )

footer.render()