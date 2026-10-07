import streamlit as st

import datetime
from src.services.get_moneyline import get_moneyline

file = st.file_uploader(
    label="Upload Moneyline",
    type="mhtml"
)

if file is not None:
    timestamp = datetime.datetime.now()
    moneyline = get_moneyline(
        file=file,
        timestamp=timestamp
    )

    if moneyline["error"]:
        st.error(moneyline["error"])
    else:
        st.write(moneyline["content"])