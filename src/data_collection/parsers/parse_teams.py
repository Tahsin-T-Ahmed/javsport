def parse_teams(title: str) -> str:
    title_splitter = None
    if "@" in title:
        title_splitter = "@"
    elif "at" in title:
        title_splitter = "at"
    elif "vs." in title:
        title_splitter = "vs."
    elif "vs" in title:
        title_splitter = "vs"
    else:
        return dict(
            error = f"ERROR (Teams-Parser): No valid OPPONENT-INDICATOR found in match title ({title})",
            content = None
        )

    title_terms = title.split(title_splitter)

    teams = [term.strip() for term in title_terms]
    teams_string = '-'.join(teams)

    return teams_string