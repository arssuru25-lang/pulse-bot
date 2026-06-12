import requests
import json

USERNAME = "arssuru25-lang"

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url)
repos = response.json()

projects = []

for repo in repos:
    projects.append({
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"]
    })

with open("projects.json", "w") as f:
    json.dump(projects, f, indent=4)

print("projects.json generated")