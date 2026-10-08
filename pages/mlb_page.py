from datetime import datetime
from src.components import sport_wagers_page
from src.data_collection.data_maps import RequiredFileMap
from src.data_collection.parsers.scan_mlb_starting_pitchers import scan_mlb_starting_pitchers
from src.metrics_assembly.assemble_mlb_metrics import assemble_mlb_metrics
from src.services.get_innings_pitched import get_innings_pitched
from src.services.get_mlb_probables import get_mlb_probables
from src.services.get_moneyline import get_moneyline
from src.services.get_siera import get_siera

timestamp = datetime.now()

sport_wagers_page.render(
    timestamp=timestamp,
    sport_name="MLB",
    sport_subheader="Pro Baseball",
    sport_icon=":material/sports_baseball:",
    schedule_url="https://www.teamrankings.com/mlb/schedules/season/?week=0",
    leaderboard_urls_dict=dict(
        at_bats_per_game="https://www.teamrankings.com/mlb/stat/at-bats-per-game",
        hits_per_game="https://www.teamrankings.com/mlb/stat/hits-per-game",
        home_runs_per_game="https://www.teamrankings.com/mlb/stat/home-runs-per-game",
        runs_per_game="https://www.teamrankings.com/mlb/stat/runs-per-game",
        total_bases_per_game="https://www.teamrankings.com/mlb/stat/total-bases-per-game",
        walks_per_game="https://www.teamrankings.com/mlb/stat/walks-per-game"
    ),
    win_trends_url="https://www.teamrankings.com/mlb/trends/win_trends/",
    required_files_list=[
        RequiredFileMap(
            file_label="Moneyline",
            file_key="moneyline",
            file_type="mhtml",
            source_url="https://www.teamrankings.com/mlb/odds/",
            file_parser=get_moneyline,
            guide_type="webpage"
        ),
        RequiredFileMap(
            file_label="Pitchers IP",
            file_key="innings_pitched",
            file_type="xlsx",
            file_parser=get_innings_pitched,
            source_url=f"https://www.fangraphs.com/leaders/major-league?pos=all&lg=all&qual=0&season={timestamp.year}&season1={timestamp.year}&ind=0&rost=0&filter=&players=0&pageitems=2000000000&stats=sta&team=0&type=c%2C13&month=33&v_cr=202301",
            guide_type="spreadsheet"
        ),
        RequiredFileMap(
            file_label="Pitchers SIERA",
            file_key="siera",
            file_type="xlsx",
            file_parser=get_siera,
            source_url=f"https://www.fangraphs.com/leaders/major-league?pos=all&lg=all&qual=0&season={timestamp.year}&season1={timestamp.year}&ind=0&rost=0&filter=&players=0&pageitems=2000000000&stats=sta&team=0&type=c%2C122&month=3&v_cr=202301",
            guide_type="spreadsheet"
        ),
        RequiredFileMap(
            file_label="Probable Pitchers",
            file_key="probable_pitchers",
            file_type="html",
            file_parser=get_mlb_probables,
            source_url="https://www.fangraphs.com/roster-resource/probables-grid",
            guide_type="spreadsheet"
        ),
        RequiredFileMap(
            file_label="Roster",
            file_key="starting_pitchers",
            file_type="xlsx",
            file_parser=scan_mlb_starting_pitchers,
            source_url="https://www.fangraphs.com/roster-resource/roster-grid",
            guide_type="spreadsheet"
        )
    ],
    metrics_assembler=assemble_mlb_metrics
)