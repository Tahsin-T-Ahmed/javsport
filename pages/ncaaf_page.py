from datetime import datetime
from src.components import sport_wagers_page
from src.data_collection.data_maps import RequiredFileMap
from src.metrics_assembly.assemble_ncaaf_metrics import assemble_ncaaf_metrics
from src.services.get_moneyline import get_moneyline

timestamp = datetime.now()

sport_wagers_page.render(
    timestamp=timestamp,
    sport_name="NCAAF",
    sport_subheader="College Football",
    sport_icon=":material/sports_football:",
    schedule_url="https://www.teamrankings.com/ncf/schedules/season/?week=0",
    leaderboard_urls_dict=dict(
        dfei=f"https://bcftoys.com/{timestamp.year}-dfei",
        field_goal_attempts_per_game="https://www.teamrankings.com/college-football/stat/field-goal-attempts-per-game",
        first_downs_per_game=f"https://cfbstats.com/{timestamp.year}/leader/national/team/offense/split01/category13/sort01.html",
        giveaways_per_game="https://www.teamrankings.com/college-football/stat/giveaways-per-game",
        punt_attempts_per_game="https://www.teamrankings.com/college-football/stat/punt-attempts-per-game",
        yards_per_game="https://www.teamrankings.com/college-football/stat/yards-per-game"
    ),
    win_trends_url="https://www.teamrankings.com/ncf/trends/win_trends/",
    team_roster_url="https://www.teamrankings.com/ncf/teams/",
    required_files_list=[
        RequiredFileMap(
            file_label="Moneyline",
            file_key="moneyline",
            file_type="mhtml",
            source_url="https://www.teamrankings.com/ncf/odds/",
            file_parser=get_moneyline,
            guide_type="webpage"
        )
    ],
    metrics_assembler=assemble_ncaaf_metrics
)