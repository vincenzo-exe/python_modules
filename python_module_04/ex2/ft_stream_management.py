#!/usr/bin/python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str]

    try:
        file = open(filename, "r")
    except OSError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        return

    print("---")
    content = file.read()
    print(content, end="")
    print("---")

    file.close()
    print(f"File '{filename}' closed.")

    transformed = content.replace("\n", "#\n")

    if transformed and transformed[-1] != "\n":
        transformed += "#"

    print("Transform data:")
    print("---")
    print(transformed, end="")
    print("---")

    print("Enter new file name (or empty): ", end="")
    output_filename = sys.stdin.readline().rstrip("\n")

    if not output_filename:
        print("Data not saved.")
        return

    print(f"Saving data to '{output_filename}'")

    output_file: typing.IO[str]

    try:
        output_file = open(output_filename, "w")
    except OSError as e:
        print(f"[STDERR] Error opening file '{output_filename}': {e}",
              file=sys.stderr)
        print("Data not saved.")
        return

    output_file.write(transformed)
    output_file.flush()
    output_file.close()

    print(f"Data saved in file '{output_filename}'.")


if __name__ == "__main__":
    main()
