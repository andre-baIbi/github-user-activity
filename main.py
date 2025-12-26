from argparse import ArgumentParser

from requests import HTTPError

from core.ActivityUtils import getEventTypeDict, showEventsPerType, showActivityByEventType
from core.GithubHandler import getEventsOfUserFromGithubApi


def printActivityUseCase(username: str):
    try:
        # 1 : Map events
        eventList = getEventsOfUserFromGithubApi(username)

        # 2: Load and show activity
        eventTypeDict = getEventTypeDict(eventList)
        print(f"{username}'s events:")
        showEventsPerType(eventTypeDict)
        showActivityByEventType(eventTypeDict)

    except HTTPError as e:
        if "404" in str(e):
            print("[ERROR] Username was NOT found!")
        else:
            print(f"[ERROR] {e}")


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument("username")

    usernameFromParams = parser.parse_args().username

    printActivityUseCase(usernameFromParams)