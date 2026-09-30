from src.components import header
from src.data_collection.data_maps import RequiredFileMap
from src.services.predict_mlb_match import predict_mlb_match
import streamlit as st

def render(
    sport_key: str,
    sport_title: str,
    required_files_list: list[RequiredFileMap]
):
    if not st.session_state[sport_key]["file_requirements"]["fulfilled"]:
        header.render(
            text="Files required:",
            text_alignment="left"
        )

        for file in required_files_list:
            color = None
            icon = None

            if st.session_state[sport_key]["file_requirements"]["data"][file["file_key"]] is not None:
                color = "green"
                icon = ":material/check:"
            else:
                color = "orange"
                icon = ":material/upload:"
            st.write(f"- :{color}[{sport_title} {file['file_label']} {icon}]")

        return

    league_avg_runs = st.session_state[sport_key]["leaderboards"]["runs_per_game"]["OVERALL"].mean()

    st.session_state[sport_key]["schedule"]["data"].apply(
        func=lambda row: st.write(
            predict_mlb_match(
                match_row=row,
                league_avg_runs=league_avg_runs,
                probable_pitchers_df=st.session_state["mlb"]["file_requirements"]["data"]["probable_pitchers"],
                sp_df=st.session_state["mlb"]["file_requirements"]["data"]["starting_pitchers"],
                siera_df=st.session_state["mlb"]["file_requirements"]["data"]["siera"],
                innings_pitched_df=st.session_state["mlb"]["file_requirements"]["data"]["innings_pitched"],
                leaderboards=st.session_state["mlb"]["leaderboards"]
            )
        ),
        axis=1
    )