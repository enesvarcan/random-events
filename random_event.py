import random as r


def calculate_sum(events):
    weights = events.values()
    sum = 0
    for w in weights:
        sum = sum + w
    return sum


def return_random_event(events):
    random_number = r.uniform(0, calculate_sum(events))
    total = 0

    for event, weight in events.items():
        total = total + weight
        if total > random_number:
            return event


events = {"Event-1": 20, "Event-2": 30, "Event-3": 20, "Event-4": 5, "Event-5": 10, "Event-6": 1}

print(return_random_event(events))
