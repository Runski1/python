import requests
query = "https://api.chucknorris.io/jokes/random"
response = requests.get(query).json()
print(response["value"])
