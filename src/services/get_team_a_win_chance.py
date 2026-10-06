import requests
import pandas as pd
from src.data_collection.data_maps import FloatMap

def get_team_a_win_chance(
    sport_key: str,
    metrics_df: pd.DataFrame,
    league_average: float | str
) -> FloatMap:
    api_url = f"http://127.0.0.1:5000/{sport_key}/predict-team-a-win-chance"
    
    metrics_json = metrics_df.to_json()

    params = dict(
        league_average=league_average,
        metrics_json=metrics_json
    )

    response = requests.get(
        url=api_url,
        params=params
    )

    if 200 != response.status_code:
        return FloatMap(
            error=f"ERROR: Invalid status code {response.status_code} from URL {api_url}",
            content=None
        )    

    team_a_win_chance = float(response.text)

    return FloatMap(
        error=None,
        content=team_a_win_chance
    )