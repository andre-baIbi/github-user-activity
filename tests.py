import Event
import EventHandler
from core.GithubHandler import fetchAllEventsOfPublicUser
from main import printAllEventsOfUsername


def test_print():
    username = "kamranahmedse"
    printAllEventsOfUsername(username)
