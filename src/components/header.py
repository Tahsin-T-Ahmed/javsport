import streamlit as st

def render(
    text: str,
    text_alignment: str = "center"
):
    st.markdown(
        body=f"#### :violet[{text}]",
        text_alignment=text_alignment,
        anchors=False
    )