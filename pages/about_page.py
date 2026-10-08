from src.components import page_header_banner
import streamlit as st

st.set_page_config(
    page_title="About JavSport"
)

page_header_banner.render(
    title="About",
    subheader="What is JavSport? Who are we?",
    icon=":material/help:"
)

with st.expander(
    label="About JavSport",
    expanded=True
):
    st.markdown("##### JavSport is a :rainbow[SPORTS-BETTING WAGER-CALCULATION SOFTWARE!]")
    st.write("Sports include baseball, basketball, and American football")
    st.write("Our strategy is to bet against the market's :green[Money-Line Odds]")
    st.write("JavSport uses a specialized formula for sports-metrics calculation")
    st.write("Our predictions are then compared with the market's to show you the edge")
    st.write("Then, you make money!")
    st.caption("or you lose, we don't know")