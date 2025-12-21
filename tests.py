import Event
import EventHandler
from core.GithubHandler import fetchAllEventsOfPublicUser


def test_print():
    username = "kamranahmedse"
    eventList = fetchAllEventsOfPublicUser(username)

    for event in eventList:
        eventObject = EventHandler.getEvent(event)

    for _, eventObj in Event.getAllEvents().items():
        print(eventObj.showEventDetails())
