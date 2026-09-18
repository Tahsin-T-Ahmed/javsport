from datetime import datetime
from src.components import delay_disclaimer, empty_schedule_notifier, timestamp_banner
from src.services.get_sport_data import get_sport_data
import streamlit as st

def load_button_handler(
    sport_key: str,
    timestamp: datetime.datetime | None,
    schedule_url: str,
    leaderboard_urls_dict: dict,
    winloss_url: str | None = None
):
    if not timestamp:
        timestamp = datetime.now()
    
    st.session_state[sport_key]["timestamp"] = timestamp

    sport_data_map = get_sport_data(
        timestamp = st.session_state[sport_key]["timestamp"],
        schedule_url = schedule_url,
        leaderboard_urls_dict = leaderboard_urls_dict,
        winloss_url = winloss_url
    )

    if sport_data_map["error"]:
        st.error(sport_data_map["error"])
        return

    st.session_state[sport_key]["data"] = sport_data_map["content"]

def render(
    sport_name: str,
    sport_subheader: str,
    sport_icon: str,
    schedule_url: str,
    leaderboard_urls_dict: dict,
    winloss_url: str | None = None,
    timestamp: datetime.datetime | None = None
):
    sport_title, sport_key = sport_name.upper(), sport_name.lower()

    st.set_page_config(
        page_title = f"JavSport - Wager {sport_title}",
        layout = "centered"
    )

    st.header(
        body = f"JavSport - {sport_title}",
        text_alignment = "center"
    )

    st.markdown(
        body = f"#### {sport_icon} {sport_subheader} {sport_icon}",
        text_alignment = "center"
    )

    st.divider()

    if sport_key not in st.session_state:
        st.session_state[sport_key] = dict()

    if "data" not in st.session_state[sport_key]:
        st.session_state[sport_key] = dict()
        
        st.markdown(
            body = "Click below to see today's predictions",
            text_alignment = "center"
        )
    else:
        timestamp_banner.render(
            timestamp = st.session_state[sport_key]["timestamp"],
            header = "Loaded on (TIMESTAMP):"
        )

        if st.session_state[sport_key]["data"]["schedule"].empty:
            empty_schedule_notifier.render(
                sport_name = sport_title,
                timestamp = st.session_state[sport_key]["timestamp"]
            )
        else:
            view_tabs = st.tabs(["Results", "Data"])

            with view_tabs[1]:
                st.markdown(
                    body = f"#### SCHEDULE ({st.session_state[sport_key]['data']['schedule'].shape[0]} games)",
                    text_alignment = "center"
                )

                st.dataframe(
                    data = st.session_state[sport_key]["data"]["schedule"],
                    hide_index = True
                )

                st.markdown(
                    body = "#### LEADERBOARDS",
                    text_alignment = "center"
                )

                for lb_key, leaderboard in st.session_state[sport_key]["data"]["leaderboards"].items():
                    st.write(f"{lb_key.upper()}:")

                    st.dataframe(
                        data = leaderboard,
                        hide_index = True
                    )

    load_button_label = f":material/touch_app: Load {sport_title} Wagers :material/touch_app:"

    if sport_key in st.session_state and "data" in st.session_state[sport_key]:
        load_button_label = f":material/refresh: Reload {sport_title} Wagers :material/refresh:"

    st.button(
        type = "primary",
        label = load_button_label,
        width = "stretch",
        on_click = load_button_handler,
        args = [sport_key, timestamp, schedule_url, leaderboard_urls_dict, winloss_url]
    )

    delay_disclaimer.render()