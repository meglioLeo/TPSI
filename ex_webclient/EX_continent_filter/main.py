import requests
import json
import pprint

url = "https://dummy-json.mock.beeceptor.com/continents"
headers = {"Accept" : "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    
    continents = json.loads(response.text)
    
    #pprint.pprint(continents)
    #print("-----------------------------")
    
    max_population_continent = None
    
    for continent in continents:
        if max_population_continent == None:
            max_population_continent = continent
        elif continent["population"] > max_population_continent["population"]:
            max_population_continent = continent
        
    pprint.pprint(max_population_continent)
    
else:
    print("Error: ", response.status_code)