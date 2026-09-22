from src.components import sport_wagers_page

sport_wagers_page.render(
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
    required_files_list=[        
        dict(
            file_name="Moneyline",
            file_type="mhtml",
            source_url="https://www.teamrankings.com/nba/odds/"
        ),
    ]
)