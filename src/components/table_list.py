from src.components import header, table

def render(
    dataframes_dict: dict,
    title: str | None = None,
    collapse: bool = False,
    hide_index:bool = False
):
    if title:
        header.render(title)
    
    for df_key, df in dataframes_dict.items():        
        table.render(
            data=df,
            label=f"{' '.join([term.capitalize() for term in df_key.split('_')])}",
            collapse=collapse,
            hide_index=hide_index
        )