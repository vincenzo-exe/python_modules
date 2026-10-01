#!/usr/bin/python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str]

    try:
        file = open(filename, "r")
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("---")
    content = file.read()
    print(content, end="")
    print("---")

    file.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
