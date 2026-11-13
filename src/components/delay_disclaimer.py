import streamlit as st

def render():
    st.markdown(
        body=":blue[:material/hourglass_top:] This data is not real-time and may take a few seconds to load :green[:material/hourglass_bottom:]",
        text_alignment="center"
    )

    st.markdown(
        body=":orange[:material/podcasts:] Wager with caution, especially when live-betting :red[:material/live_tv:]",
        text_alignment="center"
    )