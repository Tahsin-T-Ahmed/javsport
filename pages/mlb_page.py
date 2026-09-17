from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer, empty_schedule_notifier, timestamp_banner
from src.services.get_sport_data import get_sport_data

st.set_page_config(
    page_title = "JavSport - Wager MLB",
    layout = "wide"
)

st.header(
    body = "JavSport - MLB",
    text_alignment = "center"
)

st.markdown(
    body = "#### :material/sports_baseball: Pro Baseball :material/sports_baseball:",
    text_alignment = "center"
)

st.divider()

moneyline_col, siera_col = st.columns(2)

with moneyline_col:
    st.text_area("Enter Moneyline Data:")
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with siera_col:
    st.text_area("Enter SIERA Data:")
    
    st.button(
        label = "Parse SIERA Data",
        width = "stretch"
    )

def load_button_handler():
    st.session_state["mlb"] = dict(
        timestamp = datetime.now()
    )

    sport_data_map = get_sport_data(
        timestamp = st.session_state["mlb"]["timestamp"],
        schedule_url = "https://www.teamrankings.com/mlb/schedules/season/?week=0",
        leaderboard_urls_dict = dict(
            at_bats_per_game = "https://www.teamrankings.com/mlb/stat/at-bats-per-game",
            hits_per_game = "https://www.teamrankings.com/mlb/stat/hits-per-game",
            home_runs_per_game = "https://www.teamrankings.com/mlb/stat/home-runs-per-game",
            total_bases_per_game = "https://www.teamrankings.com/mlb/stat/total-bases-per-game",
            walks_per_game = "https://www.teamrankings.com/mlb/stat/walks-per-game"
        ),
        winloss_url = "https://www.teamrankings.com/mlb/trends/win_trends/"
    )

    if sport_data_map["error"]:
        st.error(sport_data_map["error"])
        return

    st.session_state["mlb"]["data"] = sport_data_map["content"]

load_button_col = st.columns([1, 2, 1])[1]

with load_button_col:
    if "mlb" not in st.session_state:
        st.markdown(
            body = "Click below to see today's predictions",
            text_alignment = "center"
        )

    load_button_label = ":material/touch_app: Load MLB Wagers :material/touch_app:"

    if "mlb" in st.session_state:
        load_button_label = ":material/refresh: Reload MLB Wagers :material/refresh:"
    
    load_button = st.button(
        type = "primary",
        label = load_button_label,
        width = "stretch",
        on_click = load_button_handler
    )

if "mlb" in st.session_state:
    with load_button_col:
        timestamp_banner.render(
            timestamp = st.session_state["mlb"]["timestamp"]
        )

    if st.session_state["mlb"]["data"]["schedule"].empty:
        empty_schedule_notifier.render(
            sport_name = "MLB",
            timestamp = st.session_state["mlb"]["timestamp"]
        )

    else:
        for key, value in st.session_state["mlb"]["data"].items():
            key

            if isinstance(value, dict):
                for k2, v2 in value.items():
                    k2
                    v2
                continue

            value

    st.divider()

delay_disclaimer.render()