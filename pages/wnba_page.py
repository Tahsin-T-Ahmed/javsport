from src.components import sport_wagers_page
from src.data_collection.scrapers.scan_moneyline import scan_moneyline

sport_wagers_page.render(
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
    required_files_list=[
        dict(
            file_label="Moneyline",
            file_key="moneyline",
            file_type="mhtml",
            callback_handler=scan_moneyline,
            source_url="https://www.teamrankings.com/wnba/odds/"
        )
    ]
)