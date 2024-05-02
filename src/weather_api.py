import requests


def get_city_coordinates(city):
    api_url = "https://geocoding-api.open-meteo.com/v1/search?name=" + city

    response = requests.get(api_url).json()

    return response


def get_weather_forecast(latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(api_url).json()
    return response


city = "Wesel"
city_coordinates = get_city_coordinates(city)
latitude = city_coordinates["results"][0]["latitude"]
longitude = city_coordinates["results"][0]["longitude"]

print(
    "The coordinates of",
    city,
    "are: longitude:",
    longitude,
    "and latitude:",
    latitude,
)

weather_forecast = get_weather_forecast(latitude, longitude)


time = weather_forecast["daily"]["time"]
temperature_2m_min = weather_forecast["daily"]["temperature_2m_min"]
temperature_2m_max = weather_forecast["daily"]["temperature_2m_max"]

for i in range(len(time)):
    print(
        "The weather forecast for",
        city,
        "on",
        time[i],
        "is a minimum temperature of",
        temperature_2m_min[i],
        "and a maximum temperature of",
        temperature_2m_max[i],
    )
