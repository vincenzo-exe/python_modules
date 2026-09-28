#!/usr/bin/python3


def garden_operations(n: int) -> None:
    if n == 0:
        int("abc")
    elif n == 1:
        10 / 0
    elif n == 2:
        open("/non/existent/file")
    elif n == 3:
        "plant" + 42


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully.")
    except Exception as e:
        print(f"Caught error: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
