from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import empty_schedule_notifier
from src.components import timestamp_banner
from src.data_collection.parsers.make_schedule import make_schedule
from src.services.get_leaderboards import get_leaderboards

st.set_page_config(
    page_title = "JavSport - Wager NFL",
    layout = "wide"
)

st.header(
    body = "JavSport - NFL",
    text_alignment = "center"
)

st.markdown(
    body = "#### :material/sports_football: Pro Football :material/sports_football:",
    text_alignment = "center"
)

st.divider()

moneyline_col, load_button_col = st.columns(2)

if "nfl_load_button_text" not in st.session_state:
    st.session_state["nfl_load_button_text"] = ":material/touch_app: Load NFL Wagers :material/touch_app:"

def load_button_handler():
    st.session_state["nfl_load_button_text"] = ":material/refresh: Reload NFL Wagers :material/refresh:"

    st.session_state["nfl_data"] = dict(
        timestamp = datetime.now()
    )

    schedule_map = make_schedule(
        schedule_url = "https://www.teamrankings.com/nfl/schedules/season/?week=0",
        timestamp = st.session_state["nfl_data"]["timestamp"]
    )

    if schedule_map["error"]:
        error = schedule_map["error"]
        st.error(error)
        return

    schedule = schedule_map["content"]
    st.session_state["nfl_data"]["schedule"] = schedule

    if schedule.empty:
        return

    leaderboards_map = get_leaderboards(
        timestamp = st.session_state["nfl_data"]["timestamp"],
        leaderboard_urls_dict = dict(
            plays_per_game = "https://www.teamrankings.com/nfl/stat/plays-per-game",
            yards_per_game = "https://www.teamrankings.com/nfl/stat/yards-per-game",
            first_downs_per_game = "https://www.teamrankings.com/nfl/stat/first-downs-per-game",
            opponent_penalties_per_game = "https://www.teamrankings.com/nfl/stat/opponent-penalties-per-game",
            touchdowns_per_game = "https://www.teamrankings.com/nfl/stat/touchdowns-per-game"
        )
    )

    if leaderboards_map["error"]:
        st.error(leaderboards_map["error"])
        return

    leaderboards = leaderboards_map["content"]
    st.session_state["nfl_data"]["leaderboards"] = leaderboards

with moneyline_col:
    st.text_area(
        "Enter Moneyline Data:",
        key = "nfl_moneyline_data"
    )
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with load_button_col:
    if "nfl_data" not in st.session_state:
        st.markdown(
            body = "Click below to see today's predictions",
            text_alignment = "center"
        )
        
    load_button = st.button(
        type = "primary",
        label = st.session_state["nfl_load_button_text"],
        width = "stretch",
        on_click = load_button_handler
    )

if "nfl_data" in st.session_state:
    with load_button_col:
        timestamp_banner.render(
            timestamp = st.session_state["nfl_data"]["timestamp"]
        )

    if st.session_state["nfl_data"]["schedule"].empty:
        empty_schedule_notifier.render(
            sport_name = "NFL",
            timestamp = st.session_state["nfl_data"]["timestamp"]
        )

    else:
        for key, value in st.session_state["nfl_data"].items():
            key

            if isinstance(value, dict):
                for k2, v2 in value.items():
                    k2
                    v2
                continue

            value

    delay_disclaimer.render()
else:
    with load_button_col:
        delay_disclaimer.render()