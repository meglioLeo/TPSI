import requests
import json
import pprint

url = "https://dummy-json.mock.beeceptor.com/posts"
headers = {"Accept":"application/json"}

response = requests.get(url, headers = headers)

if response.status_code == 200:
    
    posts = json.loads(response.text)
   
    filtered_posts = []
    
    for post in posts:
        if post["comment_count"] > 5:
            filtered_posts.append(post)
            
    pprint.pprint(filtered_posts)
     
else:
    print("Error: ", response.status_code) 