from src.data_collection.data_maps import FuncMap
from src.metrics_assembly.assemble_mlb_metrics import assemble_mlb_metrics as mlb_assembler
from src.metrics_assembly.assemble_nba_metrics import assemble_nba_metrics as nba_assembler
from src.metrics_assembly.assemble_ncaab_metrics import assemble_ncaab_metrics as ncaab_assembler
from src.metrics_assembly.assemble_ncaaf_metrics import assemble_ncaaf_metrics as ncaaf_assembler
from src.metrics_assembly.assemble_nfl_metrics import assemble_nfl_metrics as nfl_assembler
from src.metrics_assembly.assemble_wnba_metrics import assemble_wnba_metrics as wnba_assembler

def get_metrics_assembler(
    sport_key: str
) -> FuncMap:
    metrics_assembler = None

    match(sport_key.upper()):
        case "MLB":
            metrics_assembler = mlb_assembler
        case "NBA":
            metrics_assembler = nba_assembler
        case "NCAAB":
            metrics_assembler = ncaab_assembler
        case "NCAAF":
            metrics_assembler = ncaaf_assembler
        case "NFL":
            metrics_assembler = nfl_assembler
        case "WNBA":
            metrics_assembler = wnba_assembler
        case _:
            return FuncMap(
                error=f"ERROR (Metrics-Assembler-Getter): No metrics-assembler found for sport-key {sport_key}",
                content=None
            )

    return FuncMap(
        error=None,
        content=metrics_assembler
    )