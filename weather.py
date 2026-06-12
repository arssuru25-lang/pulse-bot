import requests
from email_alert import send_alert

def get_weather():
    try:
        url = "https://wttr.in/?format=3"
        response = requests.get(url)

        if response.status_code == 200:
            weather = response.text
            print(weather)

            send_alert(
                "Weather Update",
                f"Current weather: {weather}"
            )

            print("Email alert sent.")
            return weather

        return "Weather unavailable"

    except Exception as e:
        print("Error:", e)
        return "Weather unavailable"


get_weather()