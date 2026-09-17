from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import empty_schedule_notifier
from src.components import timestamp_banner
from src.data_collection.make_leaderboard import make_leaderboard
from src.data_collection.make_schedule import make_schedule

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

    plays_pg_map = make_leaderboard(
        leaderboard_url = "https://www.teamrankings.com/nfl/stat/plays-per-game",
        timestamp = st.session_state["nfl_data"]["timestamp"]
    )

    if plays_pg_map["error"]:
        error = plays_pg_map["error"]
        st.error(error)
        return

    plays_per_game = plays_pg_map["content"]
    st.session_state["nfl_data"]["plays_per_game"] = plays_per_game

    yards_pg_map = make_leaderboard(
        leaderboard_url = "https://www.teamrankings.com/nfl/stat/yards-per-game",
        timestamp = st.session_state["nfl_data"]["timestamp"]
    )

    if yards_pg_map["error"]:
        error = yards_pg_map["error"]
        st.error(error)
        return

    yards_per_game = yards_pg_map["content"]
    st.session_state["nfl_data"]["yards_per_game"] = yards_per_game

    firstdowns_pg_map = make_leaderboard(
        leaderboard_url = "https://www.teamrankings.com/nfl/stat/first-downs-per-game",
        timestamp = st.session_state["nfl_data"]["timestamp"]
    )

    if firstdowns_pg_map["error"]:
        error = firstdowns_pg_map["error"]
        st.error(error)
        return

    first_downs_per_game = firstdowns_pg_map["content"]
    st.session_state["nfl_data"]["first_downs_per_game"] = first_downs_per_game

    opp_penalties_pg_map = make_leaderboard(
        leaderboard_url = "https://www.teamrankings.com/nfl/stat/opponent-penalties-per-game",
        timestamp = st.session_state["nfl_data"]["timestamp"]
    )

    if opp_penalties_pg_map["error"]:
        error = opp_penalties_pg_map["error"]
        st.error(error)
        return

    opponent_penalties_per_game = opp_penalties_pg_map["content"]
    st.session_state["nfl_data"]["opponent_penalties_per_game"] = opponent_penalties_per_game

    touchdowns_pg_map = make_leaderboard(
        leaderboard_url = "https://www.teamrankings.com/nfl/stat/touchdowns-per-game",
        timestamp = st.session_state["nfl_data"]["timestamp"]
    )

    if touchdowns_pg_map["error"]:
        error = touchdowns_pg_map["error"]
        st.error(error)
        return

    touchdowns_per_game = touchdowns_pg_map["content"]
    st.session_state["nfl_data"]["touchdowns_per_game"] = touchdowns_per_game

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
            value

    delay_disclaimer.render()
else:
    with load_button_col:
        delay_disclaimer.render()