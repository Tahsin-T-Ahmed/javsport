import pandas as pd
from src.components import header, table

def render(
    schedule_df: pd.DataFrame,
    sport_title: str
):
    header.render(
        text=f"{sport_title} SCHEDULE"
    )

    n_games = schedule_df.shape[0]
    schedule_caption = f"{n_games} game{'s' if 1 != n_games else ''} scheduled"

    table.render(
        data=schedule_df,
        label=schedule_caption,
        hide_index=True,
        collapse=True,
        height="auto"
    )