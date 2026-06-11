import requests

def get_weather():
    try:
        url = "https://wttr.in/?format=3"
        response = requests.get(url)

        if response.status_code == 200:
            return response.text

        return "Weather unavailable"

    except Exception:
        return "Weather unavailable"