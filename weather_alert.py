import requests
import smtplib
from email.mime.text import MIMEText

# OpenWeather API details
API_KEY = "30fb4c8181ce37ae1c48588397e9fb37"
CITY = "Trivandrum"

# Email details
SENDER = "ars.suru786@gmail.com"
RECEIVER = "ars.suru786@gmail.com"
PASSWORD = "qarhyvvjjcmubten"


def send_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER, PASSWORD)
        server.send_message(msg)


# Fetch weather data
url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={CITY}&appid={API_KEY}&units=metric"
)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather}")

    # High temperature alert
    if temp > 35:
        send_alert(
            "Weather Alert",
            f"Temperature in {CITY} is above 35°C.\n"
            f"Current temperature: {temp}°C."
        )
        print("Email alert sent for high temperature!")

    # Rain alert
    if "rain" in weather.lower():
        send_alert(
            "Weather Alert",
            f"Rain is predicted in {CITY}.\n"
            f"Current weather: {weather}."
        )
        print("Email alert sent for rain!")

else:
    print("Unable to fetch weather.")