from src.components import sport_wagers_page

sport_wagers_page.render(
    sport_name="NFL",
    sport_subheader="Pro Football",
    sport_icon=":material/sports_football:",
    schedule_url="https://www.teamrankings.com/nfl/schedules/season/?week=0",
    leaderboard_urls_dict=dict(
        first_downs_per_game="https://www.teamrankings.com/nfl/stat/first-downs-per-game",
        opponent_penalties_per_game="https://www.teamrankings.com/nfl/stat/opponent-penalties-per-game",
        plays_per_game="https://www.teamrankings.com/nfl/stat/plays-per-game",
        points_per_game="https://www.teamrankings.com/nfl/stat/points-per-game",
        touchdowns_per_game="https://www.teamrankings.com/nfl/stat/touchdowns-per-game",
        yards_per_game="https://www.teamrankings.com/nfl/stat/yards-per-game"
    ),
    win_trends_url="https://www.teamrankings.com/nfl/trends/win_trends/",
    required_files_list=[
        dict(
            name="Moneyline",
            type="mhtml",
            label_urls_dict={
                "Odds": "https://www.teamrankings.com/nfl/odds/"
            }
        )
    ]
)