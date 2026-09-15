from bs4 import BeautifulSoup
import requests

def get_soup(url):
    response = requests.get(url)
    if 200 != response.status_code:
        return
    
    return BeautifulSoup(response.text, "html.parser")