from Event import PushEvent, IssuesEvent


def getEvent(event):
    eventType = event["type"]

    if eventType == "PushEvent":
        return PushEvent.getOrCreate(event["actor"]["login"], event["repo"]["name"])

    if eventType == "IssuesEvent":
        issuesEvent = IssuesEvent.getOrCreate(event["actor"]["login"], event["repo"]["name"])
        issuesEvent.newEventOcurrence(event["payload"]["action"])
        return issuesEvent

    return None
