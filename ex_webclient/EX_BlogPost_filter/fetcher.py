import requests
from config import API_URL
from models import PostModel

def fetch_posts():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        posts_json = response.json()
        return [PostModel.from_json(post) for post in posts_json]
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")
        return []