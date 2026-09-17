from bs4 import BeautifulSoup
import requests
from src.data_collection.data_maps import SoupMap

def get_soup(url: str) -> SoupMap:
    response = requests.get(url)
    if 200 != response.status_code:
        return dict(
            error = f"ERROR (Request): Invalid response from URL ({url})",
            content = None
        )
    
    soup = BeautifulSoup(response.text, "html.parser")

    return dict(
        error = None,
        content = soup
    )