import requests


def api_call(city_name):
    api_key = "2ae024d9a7f42336baedb7f9f92cd7f7"
    query = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=fi"
    response = requests.get(query)
    print(query)
    if response.status_code == 404:
        print("404 Not found")
        exit()
    else:
        return response


weather = api_call(input("Minkä kaupungin sään haluat?: ")).json()
print(f"Sää kaupungissa {weather['name']}: {weather['weather'][0]['description']} ja {weather['main']['temp']}\xb0C")
# C = -273.15+K
