#!/usr/bin/python3

import random


ALL_ACHIEVEMENTS = (
    "First Steps",
    "Speed Runner",
    "Treasure Hunter",
    "Boss Slayer",
    "Master Explorer",
    "Crafting Genius",
    "Sharp Mind",
    "World Savior",
    "Collector Supreme",
    "Strategist",
    "Survivor",
    "Unstoppable",
    "Hidden Path Finder",
    "Untouchable",
)


def gen_player_achievements() -> set:
    common_achievement = set(("Untouchable",))

    other_achievements = (
        "First Steps",
        "Speed Runner",
        "Treasure Hunter",
        "Boss Slayer",
        "Master Explorer",
        "Crafting Genius",
        "Sharp Mind",
        "World Savior",
        "Collector Supreme",
        "Strategist",
        "Survivor",
        "Unstoppable",
        "Hidden Path Finder",
    )

    count = random.randint(4, 8)
    selected = random.sample(other_achievements, count)

    return common_achievement.union(selected)


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = alice.union(bob, charlie, dylan)
    common_achievements = alice.intersection(
        bob, charlie, dylan
    )

    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(alice, bob, dylan)
    only_dylan = dylan.difference(alice, bob, charlie)

    all_game_achievements = set(ALL_ACHIEVEMENTS)

    alice_missing = all_game_achievements.difference(alice)
    bob_missing = all_game_achievements.difference(bob)
    charlie_missing = all_game_achievements.difference(charlie)
    dylan_missing = all_game_achievements.difference(dylan)

    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common_achievements}")

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    print(f"Alice is missing: {alice_missing}")
    print(f"Bob is missing: {bob_missing}")
    print(f"Charlie is missing: {charlie_missing}")
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    main()
