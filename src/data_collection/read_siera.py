import io
import pandas as pd

def parse_text(siera_text:str) -> pd.DataFrame:
    siera_table = pd.read_csv(
        io.StringIO(siera_text),
        sep = "\t",
        index_col = 0
    )

    return siera_table