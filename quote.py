import requests

def get_quote():
    try:
        url = "https://api.quotable.io/random"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'

        return "Stay consistent and keep learning."

    except Exception:
        return "Stay consistent and keep learning."