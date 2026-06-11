import random

def get_weather():
    weather_list = [
        "Sunny, 30°C",
        "Cloudy, 28°C",
        "Rainy, 25°C",
        "Windy, 27°C"
    ]

    return random.choice(weather_list)