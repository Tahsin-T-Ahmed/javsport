import streamlit as st

def render(
    name: str,
    pronunciation: str,
    role: str,
    img_path: str,
    img_caption: str | None = None,
    contact: str | None = None
):
    st.markdown(f"""
        <div style='display:flex; justify-content: space-evenly; align-items: center'>
            <span style='font-size: 2em; color: violet;'>{name}</span>
            <span style='font-size: 1em; color: gray'>(\"{pronunciation}\")</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        body=f":orange[{role}]",
        text_alignment="center",
        anchors=False
    )

    st.image(
        image=f"{img_path}",
        width="stretch",
        caption=img_caption
    )

    st.markdown(
        body=f"Contact: {contact}",
        text_alignment="center",
        anchors=False
    )