import requests

def get_news():
    try:
        url = "https://api.spaceflightnewsapi.net/v4/articles/?limit=1"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            return data["results"][0]["title"]

        return "No news available"

    except Exception:
        return "No news available"