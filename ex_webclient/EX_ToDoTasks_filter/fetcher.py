import requests
from config import API_URL
from models import TaskModel

class TaskFetcher:
    def __init__(self, url = API_URL):
        self.url = url
        
    def fetch_tasks(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            tasks_json = response.json()
            return [TaskModel.from_json(task) for task in tasks_json]
        except requests.exceptions.RequestException as e:
            print(f"HTTP request error: {e}")
            return []