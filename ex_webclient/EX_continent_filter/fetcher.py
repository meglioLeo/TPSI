import requests
from config import API_URL
from models import ContinentModel

class ContinentFetcher:
    def __init__(self, url=API_URL):
        self.url = url
        
    def fetch_continents(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            continnents_json = response.json()
            return[ContinentModel.from_json(continent) for continent in continnents_json]
        except requests.exceptions.RequestException as e:
            print(f"HTTP request error: {e}")
            return []