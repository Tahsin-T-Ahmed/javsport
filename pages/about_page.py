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
    st.markdown(
        body="##### JavSport is a :rainbow[SPORTS-BETTING WAGER-CALCULATION SOFTWARE!]",
        text_alignment="center",
        anchors=False
    )
    st.markdown(
        body="Sports include baseball, basketball, and American football",
        text_alignment="center",
        anchors=False
    )
    st.markdown(
        body="JavSport uses a specialized formula for sports-metrics calculation",
        text_alignment="center",
        anchors=False
    )
    st.markdown(
        body="Our strategy is to bet against the market's :green[Money-Line Odds]",
        text_alignment="center",
        anchors=False
    )
    st.markdown(
        body="We compare our predictions with the market's and show you the edge",
        text_alignment="center",
        anchors=False
    )
    st.markdown(
        body="Then, you make money!",
        text_alignment="center",
        anchors=False
    )
    st.caption(
        body="or you lose, we don't know",
        text_alignment="center"
    )

    st.markdown(
        body="[Link to GitHub Repo :material/open_in_new:](https://github.com/Tahsin-T-Ahmed/javsport)",
        text_alignment="right",
        anchors=False
    )

with st.expander(
    label="About Us",
    expanded=True
):
    lcol, rcol = st.columns(2)

    with lcol:
        with st.container(border=True):
            header.render("Javy")
            st.caption(
                body="\"Haa-Vee\"",
                text_alignment="center"
            )
            st.markdown(
                body=":orange[Sports-betting Connoisseur]",
                text_alignment="center",
                anchors=False
            )

            st.image(
                image="./img/javy.png",
                width="stretch",
                caption="Celebrating Tampa Bay's win over NY Yankees"
            )

    with rcol:
        with st.container(border=True):
            header.render("Tazy")
            st.caption(
                body="\"Tay-Zee\"",
                text_alignment="center"
            )
            st.markdown(
                body=":orange[Software Developer]",
                text_alignment="center",
                anchors=False
            )

            st.image(
                image="./img/tahsin.png",
                width="stretch",
                caption=["Makin' all kinds of gains (all kinds)"]
            )