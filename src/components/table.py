import pandas as pd
import streamlit as st

def render(
    data: pd.DataFrame,
    hide_index: bool = False,
    label: str | None = None,
    collapse: bool = False
):
    if not collapse:
        st.caption(label)
        st.dataframe(
            data=data,
            hide_index=hide_index
        )

        return
    
    with st.expander(
        label=label,
        expanded=True,
        type="compact"
    ):
        st.dataframe(
            data=data,
            hide_index=hide_index
        )