import datetime
from src.components import upload_dialog
from src.services.handle_odds_upload import handle_odds_upload
import streamlit as st

upload_dialog.render(
    file_label="Moneyline",
    file_key="moneyline",
    file_type="mhtml",
    sport_key="",
    sport_title="",
    callback_handler=handle_odds_upload,
    timestamp=datetime.datetime.now()
)