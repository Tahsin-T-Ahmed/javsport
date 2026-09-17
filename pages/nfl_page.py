from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer, empty_schedule_notifier, timestamp_banner
from src.services.get_sport_data import get_sport_data

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

def load_button_handler():
    st.session_state["nfl"] = dict(
        timestamp = datetime.now()
    )

    sport_data_map = get_sport_data(
        timestamp = st.session_state["nfl"]["timestamp"],
        schedule_url = "https://www.teamrankings.com/nfl/schedules/season/?week=0",
        leaderboard_urls_dict = dict(
            plays_per_game = "https://www.teamrankings.com/nfl/stat/plays-per-game",
            yards_per_game = "https://www.teamrankings.com/nfl/stat/yards-per-game",
            first_downs_per_game = "https://www.teamrankings.com/nfl/stat/first-downs-per-game",
            opponent_penalties_per_game = "https://www.teamrankings.com/nfl/stat/opponent-penalties-per-game",
            touchdowns_per_game = "https://www.teamrankings.com/nfl/stat/touchdowns-per-game"
        )
    )

    if sport_data_map["error"]:
        st.error(sport_data_map["error"])
        return

    st.session_state["nfl"]["data"] = sport_data_map["content"]

with moneyline_col:
    st.text_area("Enter Moneyline Data:")
    
    st.button(
        label = "Parse Moneyline Data",
        width = "stretch"
    )

with load_button_col:
    if "nfl" not in st.session_state:
        st.markdown(
            body = "Click below to see today's predictions",
            text_alignment = "center"
        )

    load_button_label = ":material/touch_app: Load NFL Wagers :material/touch_app:"

    if "nfl" in st.session_state:
        load_button_label = ":material/refresh: Reload NFL Wagers :material/refresh:"
        
    load_button = st.button(
        type = "primary",
        label = load_button_label,
        width = "stretch",
        on_click = load_button_handler
    )

if "nfl" in st.session_state:
    with load_button_col:
        timestamp_banner.render(
            timestamp = st.session_state["nfl"]["timestamp"]
        )

    if st.session_state["nfl"]["data"]["schedule"].empty:
        empty_schedule_notifier.render(
            sport_name = "NFL",
            timestamp = st.session_state["nfl"]["timestamp"]
        )

    else:
        for key, value in st.session_state["nfl"]["data"].items():
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