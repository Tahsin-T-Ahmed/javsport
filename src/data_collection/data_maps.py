from bs4 import BeautifulSoup
import pandas as pd
from typing import TypedDict, Callable

class JavSportDataMap(TypedDict):
    error: str | None

class DataFrameMap(JavSportDataMap):
    content: pd.DataFrame | None

class DictMap(JavSportDataMap):
    content: dict | None

class SoupMap(JavSportDataMap):
    content: BeautifulSoup | None

class StringMap(JavSportDataMap):
    content: str | None

class RequiredFileMap(TypedDict):
    file_label: str
    file_key: str
    file_type: str
    callback_handler: Callable
    source_url: str
    guide_desc: str | None