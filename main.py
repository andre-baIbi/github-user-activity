from argparse import ArgumentParser

import Event
import EventHandler
from core.GithubHandler import fetchAllEventsOfPublicUser

def countEventTypesFromData(data: list[dict]) -> dict:
    eventTypes = {}

    for event in data:
        type = event["type"]
        eventTypes[type] = eventTypes.get(type, 0) + 1

    return eventTypes

def printAllEventsOfUsername(username: str):
    eventList = fetchAllEventsOfPublicUser(username)
    print(f"{username}'s events:")
    for eventName, eventTimes in countEventTypesFromData(eventList).items():
        print(f"  - {eventName}: {eventTimes}")

    for event in eventList:
        eventObject = EventHandler.getEvent(event)

    for _, eventObj in Event.getAllEvents().items():
        eventObj.showEventDetails()




if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument("username")

    usernameFromParams = parser.parse_args().username

    printAllEventsOfUsername(usernameFromParams)