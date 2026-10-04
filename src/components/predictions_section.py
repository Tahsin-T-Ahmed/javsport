import requests
import pandas
from src.components import header
from src.services.generate_predictions import generate_predictions
import streamlit as st

def render(
    sport_key: str,
    metrics_assembler: callable
):
    header.render("PREDICTIONS")

    generate_predictions(
        sport_key=sport_key,
        metrics_assembler=metrics_assembler
    )