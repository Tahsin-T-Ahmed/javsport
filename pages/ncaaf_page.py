from src.components import sport_wagers_page

sport_wagers_page.render(
    sport_name="NCAAF",
    sport_subheader="College Football",
    sport_icon=":material/sports_football:",
    schedule_url="https://www.teamrankings.com/ncf/schedules/season/?week=0",
    leaderboard_urls_dict=dict(
        opponent_penalties_per_game="https://www.teamrankings.com/college-football/stat/opponent-penalties-per-game",
        plays_per_game="https://www.teamrankings.com/college-football/stat/plays-per-game",
        touchdowns_per_game="https://www.teamrankings.com/college-football/stat/offensive-touchdowns-per-game",
        yards_per_game="https://www.teamrankings.com/college-football/stat/yards-per-game"
    ),
    win_trends_url="https://www.teamrankings.com/ncf/trends/win_trends/"
)