import streamlit as st

def render(
    sport_title: str,
    sport_subheader: str,
    sport_icon: str
):

    st.header(
        body=f"JavSport - {sport_title}",
        text_alignment="center",
        anchor=False
    )

    st.markdown(
        body=f"#### {sport_icon} {sport_subheader} {sport_icon}",
        text_alignment="center",
        anchors=False
    )

    st.divider()