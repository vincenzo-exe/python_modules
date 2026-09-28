#!/usr/bin/python3

import math


def get_player_pos() -> tuple:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(',')

        try:
            x_str, y_str, z_str = parts
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(x_str)
        except ValueError as e:
            print(f"Error on parameter '{x_str}': {e}")
            continue

        try:
            y = float(y_str)
        except ValueError as e:
            print(f"Error on parameter '{y_str}': {e}")
            continue

        try:
            z = float(z_str)
        except ValueError as e:
            print(f"Error on parameter '{z_str}': {e}")
            continue

        return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")

    position = get_player_pos()

    print(f"Got a first tuple: {position}")

    x, y, z = position
    print(f"It includes: X={x}, Y={y}, Z={z}")

    distance = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    print(f"Distance to center: {round(distance, 4)}")


if __name__ == "__main__":
    main()
