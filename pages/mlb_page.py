from datetime import datetime
import streamlit as st
from src.components import delay_disclaimer
from src.components import timestamp_banner
from src.data_collection.get_leaderboard import get_leaderboard
from src.data_collection.get_schedule import get_schedule
from src.data_collection.get_winloss import get_winloss
from src.utils import format_timestamp

st.set_page_config(
    page_title = "JavSport - MLB Calculator",
    layout = "wide"
)

st.header(
    body = "JavSport - MLB :material/sports_baseball:", 
    text_alignment = "center"
)

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

if "mlb_load_button_text" not in st.session_state:
    st.session_state["mlb_load_button_text"] = "Load MLB Wagers"

def load_button_handler():
    st.session_state["mlb_load_button_text"] = "Refresh MLB Wagers"

    now = datetime.now()

    st.session_state["mlb_data"] = dict(
        timestamp = now
    )

    schedule_map = get_schedule(
        schedule_url = f"https://www.teamrankings.com/mlb/schedules/",
        timestamp = now
    )

    if schedule_map["error"]:
        error = schedule_map["error"]
        st.error(error)
        return
    
    schedule = schedule_map["content"]    
    st.session_state["mlb_data"]["schedule"] = schedule

    atbats_pg_map = get_leaderboard(
        leaderboard_url = f"https://www.teamrankings.com/mlb/stat/at-bats-per-game",
        timestamp = now
    )

    if atbats_pg_map["error"]:
        error = atbats_pg_map["error"]
        st.error(error)
        return

    at_bats_per_game = atbats_pg_map["content"]
    st.session_state["mlb_data"]["at_bats_per_game"] = at_bats_per_game

    hits_pg_map = get_leaderboard(
        leaderboard_url = f"https://www.teamrankings.com/mlb/stat/hits-per-game",
        timestamp = now
    )

    if hits_pg_map["error"]:
        error = hits_pg_map["error"]
        st.error(error)
        return

    hits_per_game = hits_pg_map["content"]
    st.session_state["mlb_data"]["hits_per_game"] = hits_per_game

    homeruns_pg_map = get_leaderboard(
        leaderboard_url = f"https://www.teamrankings.com/mlb/stat/home-runs-per-game",
        timestamp = now
    )

    if homeruns_pg_map["error"]:
        error = homeruns_pg_map["error"]
        st.error(error)
        return

    home_runs_per_game = homeruns_pg_map["content"]
    st.session_state["mlb_data"]["home_runs_per_game"] = home_runs_per_game

    totalbases_pg_map = get_leaderboard(
        leaderboard_url = f"https://www.teamrankings.com/mlb/stat/total-bases-per-game",
        timestamp = now
    )

    if totalbases_pg_map["error"]:
        error = totalbases_pg_map["error"]
        st.error(error)
        return

    total_bases_per_game = totalbases_pg_map["content"]
    st.session_state["mlb_data"]["total_bases_per_game"] = total_bases_per_game

    walks_pg_map = get_leaderboard(
        leaderboard_url = f"https://www.teamrankings.com/mlb/stat/walks-per-game",
        timestamp = now
    )

    if walks_pg_map["error"]:
        error = walks_pg_map["error"]
        st.error(error)
        return

    walks_per_game = walks_pg_map["content"]
    st.session_state["mlb_data"]["walks_per_game"] = walks_per_game

    winloss_map = get_winloss("https://www.teamrankings.com/mlb/trends/win_trends/")

    if winloss_map["error"]:
        error = winloss_map["error"]
        st.error(error)
        return

    winloss = winloss_map["content"]
    st.session_state["mlb_data"]["win_loss"] = winloss

load_button_col = st.columns([1, 2, 1])[1]

with load_button_col:
    load_button = st.button(
        type = "primary",
        label = st.session_state["mlb_load_button_text"],
        width = "stretch",
        on_click = load_button_handler
    )

if "mlb_data" in st.session_state:
    timestamp_f = format_timestamp.format(st.session_state["mlb_data"]["timestamp"])

    with load_button_col:
        timestamp_banner.render(timestamp_f)

    for key in st.session_state["mlb_data"]:
        key
        st.write(st.session_state["mlb_data"][key])

    st.divider()

delay_disclaimer.render()