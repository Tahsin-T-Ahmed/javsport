import requests
import pandas as pd
from src.data_collection.data_maps import StringMap

def get_team_a_win_chance(
    sport_key: str,
    metrics_df: pd.DataFrame,
    league_average: float | str | None = None
) -> StringMap:
    api_url = f"http://127.0.0.1:5000/{sport_key}/predict-team-a-win-chance"
    
    metrics_json = metrics_df.to_json()

    params = dict(
        league_average=league_average,
        metrics_json=metrics_json
    )

    response = None

    try:
        response = requests.get(
            url=api_url,
            params=params
        )
    except Exception as e:
        return StringMap(
            error=f":material/cloud_off: ERROR: Failed to connect to Predictions API",
            content=None
        )

    if 200 != response.status_code:
        return StringMap(
            error=f"ERROR: Invalid status code {response.status_code} from URL {api_url}",
            content=None
        )

    team_a_win_chance = response.text

    return StringMap(
        error=None,
        content=team_a_win_chance
    )