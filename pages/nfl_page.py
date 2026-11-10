from datetime import datetime
from src.components import sport_wagers_page
from src.data_collection.data_maps import RequiredFileMap
from src.metrics_assembly.assemble_nfl_metrics import assemble_nfl_metrics
from src.services.get_moneyline import get_moneyline
from src.services.get_nfl_dave import get_nfl_dave

sport_wagers_page.render(
    timestamp=datetime.now(),
    sport_name="NFL",
    sport_subheader="Pro Football",
    sport_icon=":material/sports_football:",
    schedule_url="https://www.teamrankings.com/nfl/schedules/season/?week=0",
    leaderboard_urls_dict=dict(
        field_goal_attempts_per_game="https://www.teamrankings.com/nfl/stat/field-goal-attempts-per-game",
        first_downs_per_game="https://www.teamrankings.com/nfl/stat/first-downs-per-game",
        giveaways_per_game="https://www.teamrankings.com/nfl/stat/giveaways-per-game",
        punt_attempts_per_game="https://www.teamrankings.com/nfl/stat/punt-attempts-per-game",
        yards_per_game="https://www.teamrankings.com/nfl/stat/yards-per-game"
    ),
    win_trends_url="https://www.teamrankings.com/nfl/trends/win_trends/",
    team_roster_url="https://www.teamrankings.com/nfl/teams/",
    required_files_list=[
        RequiredFileMap(
            file_label="Moneyline",
            file_key="moneyline",
            file_type="mhtml",
            source_url="https://www.teamrankings.com/nfl/odds/",
            file_parser=get_moneyline,
            guide_type="webpage"
        ),
        RequiredFileMap(
            file_label="DAVE",
            file_key="dave",
            file_type="csv",
            source_url="https://ftnfantasy.com/stats/nfl/dave",
            file_parser=get_nfl_dave
        )
    ],
    metrics_assembler=assemble_nfl_metrics
)