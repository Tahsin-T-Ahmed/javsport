from datetime import datetime
from src.components import sport_wagers_page
from src.data_collection.data_maps import RequiredFileMap
from src.services.get_moneyline import get_moneyline
from src.services.get_nba_team_xpm import get_nba_team_xpm

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
        offensive_rebounds_per_game="https://www.teamrankings.com/nba/stat/offensive-rebounds-per-game",
        opponent_defensive_rebounds_per_game="https://www.teamrankings.com/nba/stat/opponent-defensive-rebounds-per-game",
        turnovers_per_game="https://www.teamrankings.com/nba/stat/turnovers-per-game"
    ),
    win_trends_url="https://www.teamrankings.com/nba/trends/win_trends/",
    team_roster_url="https://www.teamrankings.com/nba/teams/",
    required_files_list=[
        RequiredFileMap(
            file_label="Odds",
            file_key="market_odds",
            file_type="mhtml",
            file_parser=get_moneyline,
            source_url="https://www.teamrankings.com/nba/odds/",
            guide_type="webpage"
        ),
        RequiredFileMap(
            file_label="Team XPM",
            file_key="team_xpm",
            file_type="csv",
            file_parser=get_nba_team_xpm,
            source_url="https://www.bball-index.com/nba/team-xpm",
            guide_type="spreadsheet"
        )
    ]
)