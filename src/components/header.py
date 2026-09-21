import streamlit as st

def render(text: str):
    st.markdown(
        body=f"#### :violet[{text}]",
        text_alignment="center",
        anchors=False
    )