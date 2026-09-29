#!/usr/bin/python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]

    print(f"Initial list of players: {players}")

    capitalized_players = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_players}")

    capitalized_only_players = [
        name for name in capitalized_players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only_players}")

    score_dict = {name: random.randint(0, 1000)
                  for name in capitalized_only_players}
    print(f"Score dict: {score_dict}")

    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")

    high_scores = {name: score for name,
                   score in score_dict.items() if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
