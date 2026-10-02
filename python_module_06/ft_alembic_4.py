#!/usr/bin/python3

import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Using package interface from alchemy/__init__.py")
    print(f"Testing create_air: {alchemy.create_air()}")

    print("Testing create_earth through package interface:")
    try:
        print(alchemy.create_earth())  # type: ignore[attr-defined]
    except AttributeError:
        print("AttributeError: create_earth is not exposed")


if __name__ == "__main__":
    main()
