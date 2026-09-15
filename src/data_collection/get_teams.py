from get_soup import get_soup

def get_teams(match_url:str) -> list:
    soup = get_soup(f"{match_url}")
    if not soup:
        return

    teams = soup.select("#h1-title a")
    if not teams:
        return
    
    teams = [team["href"].split("/")[-1].strip() for team in teams]

    return teams