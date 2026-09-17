from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import empty_schedule_notifier
from src.components import timestamp_banner
from src.data_collection.parsers.make_schedule import make_schedule
from src.services.get_leaderboards import get_leaderboards

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
    st.text_area(
        "Enter Moneyline Data:",
        key = "mlb_moneyline_data"
    )
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with siera_col:
    st.text_area(
        "Enter SIERA Data:",
        key = "mlb_siera_data"
    )
    
    st.button(
        label = "Parse SIERA Data",
        width = "stretch"
    )

def load_button_handler():
    st.session_state["mlb"] = dict(
        timestamp = datetime.now()
    )

    schedule_map = make_schedule(
        schedule_url = f"https://www.teamrankings.com/mlb/schedules/season/?week=0",
        timestamp = st.session_state["mlb"]["timestamp"]
    )

    if schedule_map["error"]:
        error = schedule_map["error"]
        st.error(error)
        return
    
    schedule = schedule_map["content"]
    st.session_state["mlb"]["schedule"] = schedule

    if schedule.empty:
        return

    leaderboards_map = get_leaderboards(
        timestamp = st.session_state["mlb"]["timestamp"],
        leaderboard_urls_dict = dict(
            at_bats_per_game = "https://www.teamrankings.com/mlb/stat/at-bats-per-game",
            hits_per_game = "https://www.teamrankings.com/mlb/stat/hits-per-game",
            home_runs_per_game = "https://www.teamrankings.com/mlb/stat/home-runs-per-game",
            total_bases_per_game = "https://www.teamrankings.com/mlb/stat/total-bases-per-game",
            walks_per_game = "https://www.teamrankings.com/mlb/stat/walks-per-game"
        ),
        winloss_url = "https://www.teamrankings.com/mlb/trends/win_trends/"
    )

    if leaderboards_map["error"]:
        st.error(leaderboards_map["error"])
        return

    leaderboards = leaderboards_map["content"]
    st.session_state["mlb"]["leaderboards"] = leaderboards

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

st.session_state

if "mlb" in st.session_state:
    with load_button_col:
        timestamp_banner.render(
            timestamp = st.session_state["mlb"]["timestamp"]
        )

    if st.session_state["mlb"]["schedule"].empty:
        empty_schedule_notifier.render(
            sport_name = "MLB",
            timestamp = st.session_state["mlb"]["timestamp"]
        )

    else:
        for key, value in st.session_state["mlb"].items():
            key

            if isinstance(value, dict):
                for k2, v2 in value.items():
                    k2
                    v2
                continue

            value

    st.divider()

delay_disclaimer.render()