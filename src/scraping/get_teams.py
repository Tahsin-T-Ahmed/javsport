import get_soup

def get_teams(match_url:str) -> list:
    soup = get_soup(f"{match_url}")

    teams = [team["href"].split("/")[-1].strip() for team in soup.select("#h1-title a")]

    return teams