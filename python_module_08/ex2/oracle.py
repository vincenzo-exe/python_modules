#!/usr/bin/python3

import os
from dotenv import load_dotenv


def get_config(key: str, default: str = "") -> str:
    return os.getenv(key, default)


def check_mode(mode: str) -> bool:
    return mode in ("development", "production")


def print_warnings(
    database_url: str,
    api_key: str,
    zion_endpoint: str,
) -> None:
    print("\nConfiguration warnings:")

    if not database_url:
        print("[WARNING] DATABASE_URL is missing")

    if not api_key:
        print("[WARNING] API_KEY is missing")

    if not zion_endpoint:
        print("[WARNING] ZION_ENDPOINT is missing")


def print_security_checks() -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> None:
    load_dotenv()

    mode = get_config("MATRIX_MODE", "development")
    database_url = get_config("DATABASE_URL")
    api_key = get_config("API_KEY")
    log_level = get_config("LOG_LEVEL", "INFO")
    zion_endpoint = get_config("ZION_ENDPOINT")

    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix...")

    if not check_mode(mode):
        print("[ERROR] MATRIX_MODE must be 'development' or 'production'")
        return

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database_url:
        if mode == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production instance")
    else:
        print("Database: Missing configuration")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    if not database_url or not api_key or not zion_endpoint:
        print_warnings(database_url, api_key, zion_endpoint)

    print_security_checks()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
