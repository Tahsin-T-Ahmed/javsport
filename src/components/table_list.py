import streamlit as st

def render(
    table_dict: dict,
    title: str | None = None,
    collapse: bool = False,
    hide_index:bool = False
):
    if title:
        st.markdown(
            body=f"#### {title}",
            text_alignment="center",
            anchors=False
        )
    
    for table_key, table in table_dict.items():
        table_name = f"{' '.join([term.capitalize() for term in table_key.split('_')])}"
        if collapse:
            with st.expander(
                table_name,
                expanded=True,
                type="compact"
            ):

                st.dataframe(
                    data=table,
                    hide_index=hide_index
                )

            continue

        st.caption(table_name)
        st.dataframe(
            data=table,
            hide_index=hide_index
        )
    pass