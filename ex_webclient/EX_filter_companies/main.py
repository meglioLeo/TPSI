import requests
import json

url = "https://fake-json-api.mock.beeceptor.com/companies"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    companies = response.json()
    
    filtered_companies = []
    
    for company in companies:
        if company["employeeCount"] > 2000:
            filtered_companies.append(company)
            
    print(filtered_companies)
    
else:
    print(f"Error: {response.status_code}")