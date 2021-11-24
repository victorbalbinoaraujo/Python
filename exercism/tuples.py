def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    return convert_coordinate(get_coordinate(azara_record)) == rui_record[1]

def create_record(azara_record, rui_record):
    return azara_record + rui_record if compare_records(azara_record, rui_record) else "not a match"

def clean_up(combined_record_group):
    return "\n".join([str((r[0], r[2], r[3], r[4])) for r in combined_record_group]) + "\n"
