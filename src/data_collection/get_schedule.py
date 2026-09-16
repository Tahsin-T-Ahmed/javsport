import datetime
import pandas as pd
from src.data_collection.data_maps import DataFrameMap
from src.data_collection.scan_table import scan_table

def parse_team_pred_ranks(match_title: str) -> str:
    title_terms = match_title.split(" ")

    team_pred_ranks = [term[1:] for term in title_terms if "#" in term and '#' == term[0]]

    return '-'.join(team_pred_ranks)


def get_schedule(schedule_url: str, timestamp: datetime.datetime) -> DataFrameMap:
    year, month, day = f"{timestamp.year:04d}", f"{timestamp.month:02d}", f"{timestamp.day:02d}"
    date_str = f"{year}-{month}-{day}"

    schedule_map = scan_table(f"{schedule_url}?date={date_str}")
    if schedule_map["error"]:
        return dict(
            error = schedule_map["error"],
            content = None
        )

    schedule = schedule_map["content"]

    if schedule.empty:
        return dict(
            error = None,
            content = schedule
        )

    schedule["MATCH ID"] = schedule["MATCHUP_LINK"].apply(lambda link: link.split("/")[-1])

    schedule["TIME"] = schedule["TIME"].apply(lambda row: f"{date_str} {row}")
    schedule["TIME"] = pd.to_datetime(schedule["TIME"])

    sport = schedule_url.split(".com/")[1].split("/")[0]
    sport = sport.lower()

    match(sport):
        case "ncaab":
            sport = "ncaa-basketball"
        case "ncaaf":
            sport = "college-football"
        case _:
            pass

    predictive_rankings_map = scan_table(f"https://www.teamrankings.com/{sport}/ranking/predictive-by-other/?date={date_str}")
    if predictive_rankings_map["error"]:
        return dict(
            error = predictive_rankings_map["error"],
            content = None
        )

    predictive_rankings = predictive_rankings_map["content"]
    predictive_rankings["TEAM ID"] = predictive_rankings["TEAM_LINK"].apply(
        lambda link: link.split("/")[-1]
    )

    schedule["TEAM PRED RANKS"] = schedule["MATCHUP"].apply(parse_team_pred_ranks)
    schedule[["TEAM A PRED RANK", "TEAM B PRED RANK"]] = schedule["TEAM PRED RANKS"].str.split("-", expand = True)

    schedule["TEAM A ID"] = schedule["TEAM A PRED RANK"].apply(
        lambda pred_rank_num: predictive_rankings[
            pred_rank_num == predictive_rankings["RANK"]
        ]["TEAM ID"].item()
    )

    schedule["TEAM B ID"] = schedule["TEAM B PRED RANK"].apply(
        lambda pred_rank_num: predictive_rankings[
            pred_rank_num == predictive_rankings["RANK"]
        ]["TEAM ID"].item()
    )

    desired_columns = ["MATCHUP", "TIME", "LOCATION", "TEAM A ID", "TEAM B ID", "MATCH ID"]

    schedule = schedule[desired_columns]

    return dict(
        error = None,
        content = schedule
    )