import streamlit as st

def render(
    title: str,
    subheader: str,
    icon: str
):

    st.header(
        body=f"JavSport - {title}",
        text_alignment="center",
        anchor=False
    )

    st.markdown(
        body=f"#### {icon} {subheader} {icon}",
        text_alignment="center",
        anchors=False
    )