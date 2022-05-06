from collections import Counter


def create_inventory(items):
    return dict(Counter(items))


def add_items(inventory, items):
    count = Counter(items)
    count.update(inventory)
    return dict(count)


def decrement_items(inventory, items):
    inventory_count = Counter(inventory)
    inventory_count.subtract(create_inventory(items))

    # Handling negative numbers
    return {key: max(value, 0) for key, value in inventory_count.items()}


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    return [(key, value) for key, value in inventory.items() if value > 0]
