import requests

API_key = "2ae024d9a7f42336baedb7f9f92cd7f7"
query = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=" + API_key
response = requests.get(query)
print(response)
print(response.status_code)