def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage = (voltage * current / theoretical_max_power) * 100
    if percentage   >= 80: return 'green'
    elif percentage >= 60: return 'orange'
    elif percentage >= 30: return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    status_code = temperature * neutrons_produced_per_second
    if status_code < threshold * 0.9: return 'LOW'
    elif threshold * 0.9 <= status_code <= threshold * 1.1: return 'NORMAL'
    return 'DANGER'