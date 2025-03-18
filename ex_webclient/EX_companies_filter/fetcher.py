import requests
from config import API_URL
from models import CompanyModel

class CompnayFetcher:
    def __init__(self, url = API_URL):
        self.url = url
        
    def fetch_companies(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            companies_json = response.json()
            companyModels = []
            for company in companies_json:
                companyModels.append(CompanyModel.from_json(company))
            return companyModels
        except requests.exceptions.RequestException as e:
            print(f"HTTP request error: {e}")
            return []