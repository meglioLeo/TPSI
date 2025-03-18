import requests
from config import API_URL
from models import UserModel

class UserFetcher:
    def __init__(self, url=API_URL):
        self.url = url
    
    def fetch_users(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            users_json = response.json()
            return [UserModel.from_json(user) for user in users_json]  #transforming json data into UserModel objects array
        except requests.exceptions.RequestException as e:
            print(f"HTTP request error: {e}")
            return []