#!/usr/bin/python3

from typing import List, Tuple
from ex0.factories import AquaFactory, CreatureFactory, FlameFactory
from ex1.factories import HealingCreatureFactory
from ex1.factories import TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    fighters = []

    for factory, strategy in opponents:
        creature = factory.create_base()
        fighters.append((creature, strategy))

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            fighter1, strategy1 = fighters[i]
            fighter2, strategy2 = fighters[j]

            print("* Battle *")
            print(fighter1.describe())
            print("vs.")
            print(fighter2.describe())
            print("now fight!")

            try:
                print(strategy1.act(fighter1))
                print(strategy2.act(fighter2))
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(
        [
            (FlameFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
        ]
    )

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(
        [
            (FlameFactory(), AggressiveStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
        ]
    )

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(
        [
            (AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy()),
        ]
    )


if __name__ == "__main__":
    main()
