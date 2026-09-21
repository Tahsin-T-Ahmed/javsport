from datetime import datetime
from src.components import delay_disclaimer, empty_schedule_notifier, table_list, timestamp_banner
from src.services.get_leaderboards import get_leaderboards
from src.services.get_schedule import get_schedule
import streamlit as st

def load_button_handler(
    sport_key: str,
    timestamp: datetime.datetime | None,    # for testing purposes
    schedule_url: str,
    leaderboard_urls_dict: dict,
    win_trends_url: str | None = None
):
    if not timestamp:
        timestamp = datetime.now()
    
    st.session_state[sport_key]["timestamp"] = timestamp

    schedule_dict_map = get_schedule(
        schedule_url=schedule_url,
        timestamp=timestamp
    )

    if schedule_dict_map["error"]:
        st.error(schedule_dict_map["error"])
        return

    st.session_state[sport_key]["schedule"] = schedule_dict_map["content"]

    if st.session_state[sport_key]["schedule"]["data"].empty:
        return

    leaderboards_map = get_leaderboards(
        leaderboard_urls_dict=leaderboard_urls_dict,
        timestamp=timestamp,
        win_trends_url=win_trends_url
    )

    if leaderboards_map["error"]:
        st.error(leaderboards_map["error"])
        return

    st.session_state[sport_key]["leaderboards"] = leaderboards_map["content"]

def render(
    sport_name: str,
    sport_subheader: str,
    sport_icon: str,
    schedule_url: str,
    leaderboard_urls_dict: dict,
    win_trends_url: str | None = None,
    timestamp: datetime.datetime | None = None
):
    sport_title, sport_key = sport_name.upper(), sport_name.lower()

    st.set_page_config(
        page_title=f"JavSport - Wager {sport_title}",
        layout="centered"
    )

    st.header(
        body=f"JavSport - {sport_title}",
        text_alignment="center",
        anchor=False
    )

    st.markdown(
        body=f"#### {sport_icon} {sport_subheader} {sport_icon}",
        text_alignment="center",
        anchors=False
    )

    st.divider()

    if sport_key not in st.session_state:
        st.session_state[sport_key] = dict()

    if "schedule" not in st.session_state[sport_key]:
        st.session_state[sport_key] = dict()
        
        st.markdown(
            body="Click below to see today's predictions",
            text_alignment="center"
        )
    else:
        timestamp_banner.render(
            timestamp=st.session_state[sport_key]["timestamp"],
            header="Loaded on (TIMESTAMP):"
        )

        if st.session_state[sport_key]["schedule"]["data"].empty:
            empty_schedule_notifier.render(
                sport_name=sport_title,
                timestamp=st.session_state[sport_key]["timestamp"]
            )
        else:
            view_tabs = st.tabs(["Results", "Data"])

            with view_tabs[0]:
                moneyline_data = st.file_uploader(
                    label="Upload Moneyline Data:",
                    type="mhtml"
                )

            with view_tabs[1]:
                game_pluralized = "game"
                if st.session_state[sport_key]["schedule"]["data"].shape[0] > 1:
                    game_pluralized = "games"

                st.markdown(
                    body=f"#### SCHEDULE ({st.session_state[sport_key]['schedule']['data'].shape[0]} {game_pluralized})",
                    text_alignment="center",
                    anchors=False
                )

                st.dataframe(
                    data=st.session_state[sport_key]["schedule"]["display"],
                    hide_index=True
                )

                st.divider()

                table_list.render(
                    title="LEADERBOARDS",
                    table_dict=st.session_state[sport_key]["leaderboards"],
                    collapse=True,
                    hide_index=True
                )

    load_button_label = f":material/touch_app: Load {sport_title} Wagers :material/touch_app:"

    if sport_key in st.session_state and "schedule" in st.session_state[sport_key]:
        load_button_label = f":material/refresh: Reload {sport_title} Wagers :material/refresh:"

    st.button(
        type="primary",
        label=load_button_label,
        width="stretch",
        on_click=load_button_handler,
        args=[sport_key, timestamp, schedule_url, leaderboard_urls_dict, win_trends_url]
    )

    delay_disclaimer.render()