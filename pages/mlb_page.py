from src.components import sport_wagers_page
from src.data_collection.data_maps import RequiredFileMap
from src.data_collection.scrapers.scan_odds_table import scan_odds_table

sport_wagers_page.render(
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
            callback_handler=scan_odds_table
        ),
        # RequiredFileMap(
        #     file_label="Pitcher IP",
        #     file_key="innings_pitched",
        #     file_type="xlsx",
        #     source_url="https://www.fangraphs.com/leaders/major-league?pos=all&lg=all&qual=0&season=2026&season1=2026&ind=0&rost=0&filter=&players=0&pageitems=2000000000&stats=sta&team=0&type=c%2C13&month=33&v_cr=202301"
        # ),
        # RequiredFileMap(
        #     file_label="Pitcher SIERA",
        #     file_key="siera",
        #     file_type="xlsx",
        #     source_url="https://www.fangraphs.com/leaders/major-league?pos=all&lg=all&qual=0&season=2026&season1=2026&ind=0&rost=0&filter=&players=0&pageitems=2000000000&stats=sta&team=0&type=c%2C122&month=3&v_cr=202301"
        # )
    ]
)