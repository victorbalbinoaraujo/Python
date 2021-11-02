EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time):
    return EXPECTED_BAKE_TIME - time

def preparation_time_in_minutes(layer):
    return PREPARATION_TIME * layer

def elapsed_time_in_minutes(layer, time):
    return layer * PREPARATION_TIME + time