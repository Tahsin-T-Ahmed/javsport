from datetime import datetime
from src.components import sport_wagers_page
from src.data_collection.data_maps import RequiredFileMap
from src.metrics_assembly.assemble_nba_metrics import assemble_nba_metrics
from src.services.get_moneyline import get_moneyline

sport_wagers_page.render(
    timestamp=datetime.now(),
    sport_name="NBA",
    sport_subheader="Pro Basketball",
    sport_icon=":material/sports_basketball:",
    schedule_url="https://www.teamrankings.com/nba/schedules/season/?week=0",
    leaderboard_urls_dict=dict(
        field_goals_attempted_per_game="https://www.teamrankings.com/nba/stat/field-goals-attempted-per-game",
        field_goals_made_per_game="https://www.teamrankings.com/nba/stat/field-goals-made-per-game",
        free_throws_made_per_game="https://www.teamrankings.com/nba/stat/free-throws-made-per-game",
        points_per_game="https://www.teamrankings.com/nba/stat/points-per-game",
        three_pointers_made_per_game="https://www.teamrankings.com/nba/stat/three-pointers-made-per-game"
    ),
    win_trends_url="https://www.teamrankings.com/nba/trends/win_trends/",
    team_roster_url="https://www.teamrankings.com/nba/teams/",
    required_files_list=[        
        RequiredFileMap(
            file_label="Moneyline",
            file_key="moneyline",
            file_type="mhtml",
            file_parser=get_moneyline,
            source_url="https://www.teamrankings.com/nba/odds/",
            guide_type="webpage"
        )
    ],
    metrics_assembler=assemble_nba_metrics
)