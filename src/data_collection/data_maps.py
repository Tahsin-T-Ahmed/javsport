from bs4 import BeautifulSoup
import pandas as pd
from typing import TypedDict

class JavSportDataMap(TypedDict):
    error: str | None

class DataFrameMap(JavSportDataMap):
    content: pd.DataFrame | None

class DictMap(JavSportDataMap):
    content = dict | None

class SoupMap(JavSportDataMap):
    content: BeautifulSoup | None