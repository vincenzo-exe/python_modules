#!/usr/bin/python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")

    scores = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    score_range = highest - lowest

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
