from src.components import sport_wagers_page

sport_wagers_page.render(
    sport_name = "NFL",
    sport_subheader = "Pro Football",
    sport_icon = ":material/sports_football:",
    schedule_url = "https://www.teamrankings.com/nfl/schedules/season/?week=0",
    leaderboard_urls_dict = dict(
        plays_per_game = "https://www.teamrankings.com/nfl/stat/plays-per-game",
        yards_per_game = "https://www.teamrankings.com/nfl/stat/yards-per-game",
        first_downs_per_game = "https://www.teamrankings.com/nfl/stat/first-downs-per-game",
        opponent_penalties_per_game = "https://www.teamrankings.com/nfl/stat/opponent-penalties-per-game",
        touchdowns_per_game = "https://www.teamrankings.com/nfl/stat/touchdowns-per-game"
    )
)