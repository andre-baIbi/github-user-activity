
def countEventTypesFromData(data: list[dict]) -> dict:
    eventTypes = {}

    for event in data:
        type = event["type"]
        eventTypes[type] = eventTypes.get(type, 0) + 1

    return eventTypes

def showEventsPerType(eventDict):
    for eventType, eventList in eventDict.items():
        print(f"\t{eventType}: {len(eventList)} times")

def getEventTypeDict(eventList) -> dict:
    eventTypeDict = {}

    for event in eventList:
        eventType = event["type"]
        eventTypeList = eventTypeDict.get(eventType, [])
        eventTypeList.append(event)
        eventTypeDict[eventType] = eventTypeList

    return eventTypeDict

def getReposFromEventTypeList(eventTypeList: list[dict]):
    repoDict = {}

    for event in eventTypeList:
        repoName = event["repo"]["name"]
        repoDict[repoName] = repoDict.get(repoName, 0) + 1

    return repoDict

def printWatchEventActivity(eventTypeList):
    for event in eventTypeList:
        repo = event["repo"]["name"]
        action: str = event["payload"]["action"]
        print(f"{action.title()} watching {repo}")

def printPushEventActivity(eventTypeList):
    repoDict = getReposFromEventTypeList(eventTypeList)
    for repo, numberOfPushes in repoDict.items():
        if numberOfPushes == 1:
            print(f"Pushed a new commit to {repo}")
            continue
        print(f"Pushed {numberOfPushes} commits to {repo}")

def printIssueCommentEventActivity(eventTypeList):
    repoDict = getReposFromEventTypeList(eventTypeList)
    for repo, numberOfComments in repoDict.items():
        if numberOfComments == 1:
            print(f"Commented on an issue on {repo}")
            continue
        print(f"Commented {numberOfComments} times in issues on {repo}")

def printOpenClosedEventActivity(msg, eventTypeList):
    eventsDict = {}

    for event in eventTypeList:
        repo = event["repo"]["name"]
        action: str = event["payload"]["action"]
        repoActionKey = action + ";" + repo

        eventsDict[repoActionKey] = eventsDict.get(repoActionKey, 0) + 1

    for _repoActionKey, numberOfActions in eventsDict.items():
        [action, repo] = _repoActionKey.split(";")
        print(f"{action.title()} {numberOfActions} {msg} {repo}")

def printPullRequestEvent(eventTypeList):
    msg = "pull requests on"
    printOpenClosedEventActivity(msg, eventTypeList)

def printIssuesEventActivity(eventTypeList):
    msg = "issues on"
    printOpenClosedEventActivity(msg, eventTypeList)

def printForkEvent(eventTypeList):
    for event in eventTypeList:
        destination = event["payload"]["forkee"]["full_name"]
        source = event["repo"]["name"]
        print(f"Forked a repo from {source} to {destination}")

def showActivityByEventType(eventTypeDict: dict):   #Show event activity
    printActivityActions = {
        "IssuesEvent": printIssuesEventActivity,
        "WatchEvent": printWatchEventActivity,
        "PullRequestEvent": printPullRequestEvent,
        "ForkEvent": printForkEvent,
        "PushEvent": printPushEventActivity,
        "IssueCommentEvent": printIssueCommentEventActivity,
    }

    for eventType, eventTypeList in eventTypeDict.items():
        printActivityActions[eventType](eventTypeList)