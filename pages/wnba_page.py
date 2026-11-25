from datetime import datetime
from src.components import sport_wagers_page
from src.data_collection.data_maps import RequiredFileMap
from src.services.get_moneyline import get_moneyline
from src.services.get_wnba_team_lebron import get_wnba_team_lebron

sport_wagers_page.render(
    timestamp=datetime.now(),
    sport_name="WNBA",
    sport_subheader="Women's NBA",
    sport_icon=":material/sports_basketball:",
    schedule_url="https://www.teamrankings.com/wnba/schedules/season/?week=0",
    leaderboard_urls_dict=dict(
        field_goals_attempted_per_game="https://www.teamrankings.com/wnba/stat/field-goals-attempted-per-game",
        field_goals_made_per_game="https://www.teamrankings.com/wnba/stat/field-goals-made-per-game",
        free_throws_made_per_game="https://www.teamrankings.com/wnba/stat/free-throws-made-per-game",
        points_per_game="https://www.teamrankings.com/wnba/stat/points-per-game",
        three_pointers_made_per_game="https://www.teamrankings.com/wnba/stat/three-pointers-made-per-game"
    ),
    win_trends_url="https://www.teamrankings.com/wnba/trends/win_trends/",
    team_roster_url="https://www.teamrankings.com/wnba/teams/",
    required_files_list=[
        RequiredFileMap(
            file_label="Odds",
            file_key="market_odds",
            file_type="mhtml",
            source_url="https://www.teamrankings.com/wnba/odds/",
            file_parser=get_moneyline,
            guide_type="webpage"
        ),
        RequiredFileMap(
            file_label="Team-LEBRON",
            file_key="team_lebron",
            file_type="csv",
            source_url="https://www.bball-index.com/wnba/team-ratings",
            file_parser=get_wnba_team_lebron,
            guide_type="spreadsheet"
        )
    ]
)