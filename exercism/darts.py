import math


def score(x, y):
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    return 10
