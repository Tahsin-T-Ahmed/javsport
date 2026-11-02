from src.data_collection.data_maps import StringMap

def parse_teams(title: str) -> StringMap:
    title_terms = title.strip().split(" ")
    
    title_splitter = None
    if "@" in title_terms:
        title_splitter = "@"
    elif "at" in title_terms:
        title_splitter = "at"
    elif "vs." in title_terms:
        title_splitter = "vs."
    elif "vs" in title_terms:
        title_splitter = "vs"
    else:
        return StringMap(
            error=f"ERROR (Teams-Parser): No valid OPPONENT-INDICATOR found in match title ({title})",
            content=None
        )

    title_terms = title.split(title_splitter)

    teams = [term.strip() for term in title_terms]
    teams_string = '--javsport-team-separator-str--'.join(teams)

    return StringMap(
        error=None,
        content=teams_string
    )