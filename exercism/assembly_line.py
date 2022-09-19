def production_rate_per_hour(speed):
    percentual = {
        range(1, 5) : 1,
        range(5, 9) : 0.9,
        range(9, 11) : 0.77
    }

    for k in percentual:
        if speed in k:
            return percentual[k] * speed * 221

    return 0

def working_items_per_minute(speed):
    production_rate_per_hour(speed) / 60