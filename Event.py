from abc import ABC, abstractmethod

allEvents = {}

class Event():
    actor: str
    repo: str

    def __init__(self, actor, repo):
        self.actor = actor
        self.repo = repo

    @abstractmethod
    def showEventDetails(self): ...

    @abstractmethod
    def newEventOcurrence(self, *args): ...

    @classmethod
    def getOrCreate(cls, actor, repo, *args):
        """
        Gets a push event that already happened or creates a new one.
        Adds one push to the respective event.
        :param actor: Actor of push
        :param repo: Repo of push
        :return: PushEvent
        """

        eventId = generatePushEventId(actor, repo)
        event = allEvents.get(eventId)
        if not event:
            event = cls(actor, repo)
            allEvents[generatePushEventId(actor, repo)] = event
        return event

class PushEvent(Event):
    pushes = 0

    def newEventOcurrence(self):
        self.addPush()

    def addPush(self):
        self.pushes += 1

    def showEventDetails(self):
        return str(self)

    def __str__(self):
        return f"{self.actor} has pushed {self.pushes} time(s) to repo named {self.repo}."

class IssuesEvent(Event):
    actionTypesAndOcurrences: {str : int}

    def __init__(self, actor, repo):
        super().__init__(actor, repo)
        self.actionTypesAndOcurrences = {}

    def newEventOcurrence(self, issueActionType):
        self.actionTypesAndOcurrences[issueActionType] = self.actionTypesAndOcurrences.get(issueActionType, 0) + 1

    def showEventDetails(self):
        print(f"Issues in {self.repo} ==================")
        for action, timesActionWasExecuted in self.actionTypesAndOcurrences.items():
            print(f"\t{self.actor} has {action} {timesActionWasExecuted} issues")



def getAllEvents() -> dict:
    return allEvents

def generatePushEventId(actor, repo):
    return actor + "/" + repo