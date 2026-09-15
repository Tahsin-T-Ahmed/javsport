from bs4 import BeautifulSoup
import requests

def get_soup(url:str) -> BeautifulSoup:
    response = requests.get(url)
    if 200 != response.status_code:
        return
    
    soup = BeautifulSoup(response.text, "html.parser")

    return soup