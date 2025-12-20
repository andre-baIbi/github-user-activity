import json
import requests

def fetchAllEventsOfPublicUser(username: str) -> list[dict]:
    endpoint = f"https://api.github.com/users/{username}/events"

    response = requests.get(endpoint)
    response.raise_for_status()

    return json.loads(response.text)
