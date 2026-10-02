#!/usr/bin/python3

from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print("Using 'from ... import ...' to access alchemy/elements.py")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
