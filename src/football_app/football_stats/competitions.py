from statsbombpy import sb

from typing import List
import pandas as pd
import json

def get_competitions() -> pd.DataFrame:
    return json.dumps(
        sb.competitions().to_dict(orient='records')
    )

def get_matches(competition_id: int, season_id: int) -> pd.DataFrame:
    return json.dumps(
        sb.matches(competition_id=competition_id, season_id=season_id).to_dict(orient='records')
    )