import requests


def get_city_coordinates(city):
    api_url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city

    response = requests.get(api_url).json()

    return response


city = "Berlin"
city_coordinates = get_city_coordinates(city)
latitude = city_coordinates["results"][0]["latitude"]
longitude = city_coordinates["results"][0]["longitude"]


print(
    "The coordinaten of",
    city,
    "are: longitude:",
    longitude,
    "and latitude:",
    latitude,
)
