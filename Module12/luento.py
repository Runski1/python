import requests

query = input("Anna hakusana: ")
request = "https://api.tvmaze.com/searh/shows?q=" + query


def print_show_data(show_data):
    for show in show_data:
        # Suodatetaan hakutulos näyttämään vain isoimmat match scoret
        if show["score"] > 0.5:
            print(show["show"]["name"])
            print(show["score"])


try:
    response = requests.get(request)
    print(response.status_code)
    if response.status_code == 200:
        response_content = response.json()
        print_show_data(response_content)

except requests.exceptions.RequestException as e:
    print("error")
    print(e)

