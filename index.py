import streamlit as st

home_page = st.Page(
    page = "./pages/home-page.py",
    title = "Home",
    icon = ":material/home:"
)

mlb_page = st.Page(
    page = "./pages/mlb-page.py",
    title = "MLB",
    url_path = "mlb",
    icon = ":material/sports_baseball:"
)

nba_page = st.Page(
    page = "./pages/nba-page.py",
    title = "NBA",
    url_path = "nba",
    icon = ":material/sports_basketball:"
)

ncaab_page = st.Page(
    page = "./pages/ncaab-page.py",
    title = "NCAAB",
    url_path = "ncaa-basketball",
    icon = ":material/sports_basketball:"
)

ncaaf_page = st.Page(
    page = "./pages/ncaaf-page.py",
    title = "NCAAF",
    url_path = "ncaa-football",
    icon = ":material/sports_football:"
)

nfl_page = st.Page(
    page = "./pages/nfl-page.py",
    title = "NFL",
    url_path = "nfl",
    icon = ":material/sports_football:"
)

wnba_page = st.Page(
    page = "./pages/wnba-page.py",
    title = "WNBA",
    url_path = "wnba",
    icon = ":material/sports_basketball:"
)

pages = [home_page, mlb_page, nba_page, ncaab_page, ncaaf_page, nfl_page, wnba_page]

nav = st.navigation(
    pages = pages,
    position = "top"
)

nav.run()