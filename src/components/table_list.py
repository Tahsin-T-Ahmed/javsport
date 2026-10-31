from src.components import header, table
import streamlit as st

def render(
    dataframes_dict: dict,
    title: str | None = None,
    collapse: bool = False,
    hide_index: bool = False,
    height: int | str = "auto",
    sport_title: str | None = None
):
    with st.expander(
        label=f":violet[{title}]",
        expanded=True
    ):
        if title:
            header.render(title.upper())
        
        for df_key, df in dataframes_dict.items():
            table.render(
                data=df,
                label=f"{f'{sport_title} ' if sport_title else ''}{' '.join([
                    term.capitalize()
                    if term not in ["dave", "dfei", "ofei", "siera"]
                    else term.upper()
                    for term in df_key.split('_')
                ])}",
                collapse=collapse,
                hide_index=hide_index,
                height=height
            )