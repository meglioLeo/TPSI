import requests
import json
import pprint

url = "https://dummy-json.mock.beeceptor.com/todos"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    
    list_of_tasks = json.loads(response.text)
    
    filtered_list = []
    
    for task in list_of_tasks:
        if task["completed"] == False:
            filtered_list.append(task)
            
    pprint.pprint(filtered_list)
    
else:
    print("Error: ", response.status_code)