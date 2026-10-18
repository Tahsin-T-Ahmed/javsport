from src.components import footer, founder_intro
import streamlit as st

st.set_page_config(
    page_title="About JavSport"
)

st.header(
    body="What is JavSport?",
    text_alignment="center",
    anchor=False
)
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

st.divider()

st.subheader(
    body="About Us",
    text_alignment="center"
)

lcol, rcol = st.columns(2)

with lcol:
    with st.container(border=True):
        founder_intro.render(
            name="Javy",
            pronunciation="Haa-Vee",
            role="Sports-Betting Connoisseur",
            img_path="./img/javy.png",
            img_caption="Celebrating Tampa Bay's win over NY Yankees",
            contact="dbookmvp7@gmail.com"
        )

with rcol:
    with st.container(border=True):
        founder_intro.render(
            name="Tazy",
            pronunciation="Tay-Zee",
            role="Software Developer",
            img_path="./img/tahsin.png",
            img_caption="Makin' all kinds of gains (all kinds)",
            contact="tahsin.t.ahmed@gmail.com"
        )

footer.render()