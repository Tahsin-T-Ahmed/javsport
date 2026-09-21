import pandas as pd
import streamlit as st

def render(
    schedule_df: pd.DataFrame
):    
    st.markdown(
        body=f"#### SCHEDULE",
        text_alignment="center",
        anchors=False
    )

    n_games = schedule_df.shape[0]
    st.caption(f"{n_games} game{'s' if 1 != n_games else ''} scheduled")

    st.dataframe(
        data=schedule_df,
        hide_index=True
    )