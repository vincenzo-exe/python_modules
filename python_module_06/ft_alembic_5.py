#!/usr/bin/python3

from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===")
    print("Using 'from alchemy import ...' package interface")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
