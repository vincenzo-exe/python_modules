#!/usr/bin/python3


def secure_archive(
    filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(filename, "r") as file:
                return True, file.read()
        except OSError as e:
            return False, f"{e}"

    if action == "write":
        try:
            with open(filename, "w") as file:
                file.write(content)
                return True, "Content successfully written to file"
        except OSError as e:
            return False, f"{e}"

    return False, "Invalid action. Use 'read' or 'write'"


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("archive.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("secure_archive.txt", "write", result[1]))


if __name__ == "__main__":
    main()
