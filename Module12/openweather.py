import requests


def api_call(city_name):
    api_key = "2ae024d9a7f42336baedb7f9f92cd7f7"
    query = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=fi"
    response = requests.get(query)
    return response


weather = api_call(input("Minkä kaupungin sään haluat?: ")).json()
print(f"Sää kaupungissa {weather['name']}: {weather['weather'][0]['description']} ja {weather['main']['temp']}\xb0C")
