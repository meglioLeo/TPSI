import requests
import json

url = "https://fake-json-api.mock.beeceptor.com/users"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    users = response.json()

    filtered_users = []

    for user in users:
        if user["state"]=="Illinois":
            filtered_users.append(user)

    print(filtered_users)

else:
    print("Error: {response.status_code}")