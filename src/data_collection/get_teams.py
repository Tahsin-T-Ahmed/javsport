from get_soup import get_soup
from typing import TypedDict
from src.data_collection.data_maps import ListMap

def get_teams(match_url:str) -> ListMap:
    soup_map = get_soup(f"{match_url}")
    if soup_map["error"]:
        return dict(
            error = soup_map["error"],
            content = None
        )

    soup = soup_map["content"]

    team_links = soup.select("#h1-title a")
    if not team_links:
        return dict(
            error = f"ERROR (Match-Teams): Failed to scan TEAM-LINKS from URL ({match_url})",
            content = None
        )
    
    team_ids = [team["href"].split("/")[-1].strip() for team in team_links]
    if not team_links:
        return dict(
            error = f"ERROR (Match-Teams): Failed to parse TEAM-IDs of team-links ({team_links}) from URL ({match_url})",
            content = None
        )

    return dict(
        error = None,
        content = team_ids
    )