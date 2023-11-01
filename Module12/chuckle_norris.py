import requests
import json
query = "https://api.chucknorris.io/jokes/random"
response = requests.get(query).json()
print(json.dumps(response, indent=2))
print(response["value"])
