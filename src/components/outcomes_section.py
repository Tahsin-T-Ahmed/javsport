from src.components import header, table
from src.services.get_outcomes import get_outcomes
from src.services.get_team_roster import get_team_roster
from src.services.get_win_trends import get_win_trends
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    team_roster_url: str,
    win_trends_url: str,
    winner_picks_url: str | None
):
    header.render(f"{sport_title} OUTCOMES")

    file = None

    with st.container(border=True):
        file = st.file_uploader(
            label=f"Upload :orange[{sport_title}] Wagers :green[Spreadsheet :material/view_list:]",
            type="csv"
        )

    if not file:
        return

    loading_container = st.empty()

    outcomes = None

    with loading_container.container():
        with st.spinner(
            text="Loading Outcomes...",
            show_time=True
        ):
            win_trends_df = None
            if (
                "leaderboards" in st.session_state[sport_key]
                and
                "win_trends" in st.session_state[sport_key]["leaderboards"]
            ):
                win_trends_df = st.session_state[sport_key]["leaderboards"]["win_trends"]
            else:
                wintrends_map = get_win_trends(win_trends_url)
                if wintrends_map["error"]:
                    st.error(wintrends_map["error"])
                    return
                win_trends_df = wintrends_map["content"]

            team_roster_df = None
            if "team_roster" in st.session_state[sport_key]:
                team_roster_df = st.session_state[sport_key]["team_roster"]
            else:
                team_roster_map = get_team_roster(team_roster_url)
                if team_roster_map["error"]:
                    st.error(team_roster_map["error"])
                    return
                team_roster_df = team_roster_map["content"]

            progress_bar = st.progress(
                value=0.0
            )

            outcomes_map = get_outcomes(
                file=file,
                win_trends_df=win_trends_df,
                team_roster_df=team_roster_df,
                winner_picks_url=winner_picks_url,
                progress_bar=progress_bar
            )

            if outcomes_map["error"]:
                st.error(outcomes_map["error"])
                return

            outcomes = outcomes_map["content"]

    if outcomes is None:
        return

    loading_container.empty()

    table.render(
        data=outcomes,
        label=f"{sport_title} Outcomes",
        height="auto",
        hide_index=True
    )