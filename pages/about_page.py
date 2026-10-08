from src.components import header, page_header_banner
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
    st.write("JavSport uses a specialized formula for sports-metrics calculation")
    st.write("Our strategy is to bet against the market's :green[Money-Line Odds]")
    st.write("We compare our predictions with the market's and show you the edge")
    st.write("Then, you make money!")
    st.caption("or you lose, we don't know")

    st.markdown(
        body="[Link to GitHub Repo](https://github.com/Tahsin-T-Ahmed/javsport)"
    )

with st.expander(
    label="About Us",
    expanded=True
):
    lcol, rcol = st.columns(2)

    with lcol:
        header.render("Javier Rodriguez")
        st.markdown(
            body="Sports-betting Connoisseur",
            text_alignment="center"
        )

        st.image(
            image="./img/javy.png"
        )
        st.caption("Celebrating Tampa Bay's win over NY Yankees")

    with rcol:
        header.render("Tahsin T Ahmed")
        st.markdown(
            body="Software Developer",
            text_alignment="center"
        )

        st.image(
            image="./img/tahsin.png"
        )
        st.caption("Makin' all kinds of gains (all kinds)")