#!/usr/bin/python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}

    for parameter in sys.argv[1:]:
        parts = parameter.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item, quantity_str = parts

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory[item] = quantity

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    if not inventory:
        print("Inventory is empty.")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
        return

    for item in items:
        percentage = round(inventory[item] / total * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant_item = items[0]
    least_abundant_item = items[0]

    for item in items[1:]:
        if inventory[item] > inventory[most_abundant_item]:
            most_abundant_item = item

        if inventory[item] < inventory[least_abundant_item]:
            least_abundant_item = item

    print(f"Item most abundant: {most_abundant_item} "
          f"with quantity {inventory[most_abundant_item]}")
    print(f"Item least abundant: {least_abundant_item} "
          f"with quantity {inventory[least_abundant_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
